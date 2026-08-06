# Employee Expense Management (EEM)

This project provides a local end-to-end implementation of the EEM architecture:

`Streamlit -> FastAPI -> CrewAI Flow -> receipt/policy/risk/manager/employee agents`

The JSON endpoint `POST /v1/expenses` is the Power Automate integration point.
The multipart endpoint `POST /submit-expense` is kept for the Streamlit client.

## 1. Create the environment

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Set `API_KEY` and `GROQ_API_KEY` in `.env`. The default model is the Groq
OpenAI-compatible model `groq/llama-3.3-70b-versatile`; change `MODEL_NAME`
and the key if using another LiteLLM provider.

## 2. Start the FastAPI service

From the project directory:

```powershell
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

Check `http://localhost:8000/` and `http://localhost:8000/docs`.

## 3. Start Streamlit

In a second terminal:

```powershell
streamlit run app.py
```

The Streamlit client sends the receipt as multipart form data. Power Automate
should send JSON to `/v1/expenses` with the `x-api-key` header and a base64
encoded receipt. The response contains the final CrewAI recommendation.

## 4. Power Automate mapping

Configure an HTTP action with:

- Method: `POST`
- URI: `https://<service-host>/v1/expenses`
- Header: `x-api-key: <API_KEY>`
- JSON fields: employee details, amount, expense type, receipt name, and
  `receipt_base64`

The approval branch can route `AUTO_APPROVE`, `MANAGER_REVIEW`, and `REJECT`
to the corresponding Power Automate actions. Persist the returned request and
decision in Dataverse/SQL, then expose those records in Power BI.

## Cache-breakpoint fix

`compat.py` is loaded before CrewAI and wraps LiteLLM's completion boundary.
It recursively removes the provider-unsupported `cache_breakpoint` field and
enables LiteLLM parameter dropping. This avoids modifying Streamlit or
FastAPI internals and works for both direct and Flow-triggered calls.

## Run checks

```powershell
python -m compileall -q .
pytest -q
```

The application still requires a valid model API key for a real CrewAI run.

## Deploy with GitHub and Streamlit Community Cloud

Commit the project to GitHub, excluding `.env` and generated folders. Deploy
`app.py` in Streamlit Community Cloud. In the Streamlit app settings, add these
secrets:

```toml
API_KEY = "the-same-key-used-by-the-api"
EEM_API_URL = "https://your-fastapi-service.onrender.com"
```

Streamlit Community Cloud hosts the UI only. Deploy the FastAPI/CrewAI service
separately; the included `render.yaml` can be used with Render. Set `API_KEY`,
`GROQ_API_KEY`, `MODEL_NAME`, and `UPLOAD_FOLDER` in the backend service
environment. After deployment, put the backend HTTPS URL in the Streamlit
`EEM_API_URL` secret and redeploy the Streamlit app.
