"""Runtime compatibility helpers for CrewAI/LiteLLM integrations.

Some LiteLLM providers reject the Anthropic-only ``cache_breakpoint`` field.
CrewAI can add that field to message dictionaries before dispatching a request.
This small adapter removes it at the provider boundary and leaves all other
request data unchanged.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

# Keep CrewAI's local vector/memory files inside the project and avoid a
# machine-specific AppData location that may be unavailable in cloud runners.
os.environ.setdefault("CREWAI_STORAGE_DIR", str(Path.cwd() / ".crewai"))
if os.name == "nt":
    # CrewAI 1.15 creates an encrypted credentials directory at import time.
    # Keeping it project-local makes the service work in restricted runners
    # and avoids a stale/unwritable global credentials folder.
    os.environ["LOCALAPPDATA"] = str(Path.cwd() / ".localappdata")


def _strip_cache_breakpoints(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: _strip_cache_breakpoints(item)
            for key, item in value.items()
            if key != "cache_breakpoint"
        }
    if isinstance(value, list):
        return [_strip_cache_breakpoints(item) for item in value]
    if isinstance(value, tuple):
        return tuple(_strip_cache_breakpoints(item) for item in value)
    return value


def install_litellm_compatibility() -> None:
    """Install the shim once, without changing application-level prompts."""
    try:
        import litellm
    except ImportError:
        return

    if getattr(litellm, "_eem_cache_breakpoint_shim", False):
        return

    real_completion = litellm.completion

    def completion(*args: Any, **kwargs: Any) -> Any:
        return real_completion(
            *[_strip_cache_breakpoints(arg) for arg in args],
            **_strip_cache_breakpoints(kwargs),
        )

    litellm.completion = completion
    litellm.drop_params = True
    litellm._eem_cache_breakpoint_shim = True
