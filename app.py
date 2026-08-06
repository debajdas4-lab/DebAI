import os
from html import escape

import streamlit as st
import requests

# Streamlit Cloud stores secrets in st.secrets rather than .env. Copy only
# known application settings into the environment before Config is imported.
try:
    for _key in (
        "API_KEY", "EEM_API_URL", "APP_NAME", "APP_VERSION", "MODEL_NAME",
        "LLM_PROVIDER", "GROQ_API_KEY", "TEMPERATURE",
    ):
        if _key in st.secrets and not os.getenv(_key):
            os.environ[_key] = str(st.secrets[_key])
except FileNotFoundError:
    pass

from config import Config


def render_employee_guidance(text: str) -> None:
    """Render model output as safe, readable HTML in Streamlit."""
    paragraphs = [
        f"<p>{'<br>'.join(escape(line) for line in paragraph.splitlines())}</p>"
        for paragraph in text.split("\n\n")
        if paragraph.strip()
    ]
    st.markdown(
        """
        <style>
        .guidance-card {
            background: #f8fafc;
            border: 1px solid #dbe3ec;
            border-left: 5px solid #2563eb;
            border-radius: 10px;
            padding: 1rem 1.25rem;
            line-height: 1.6;
            color: #172033;
        }
        .guidance-card p { margin: 0 0 .9rem 0; }
        .guidance-card p:last-child { margin-bottom: 0; }
        </style>
        <div class="guidance-card">
        """ + "".join(paragraphs) + "</div>",
        unsafe_allow_html=True,
    )

st.set_page_config(
    page_title="Expense AI Assistant",
    page_icon="💳",
    layout="wide"
)
from pathlib import Path
from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="Employee Expense Management",
    page_icon="💼",
    layout="wide"
)

image_path = Path(__file__).parent / "expense.jpg"

if image_path.exists():
    image = Image.open(image_path)

    # Center the image and keep its complete aspect ratio
    left, center, right = st.columns([1, 3, 1])

    with center:
        st.image(
            image,
            width=900
        )
else:
    st.warning("Hero image not found.")
    
st.title("💳 Expense AI Assistant")

st.write(
    "Submit your expense report for AI-powered compliance "
    "and approval recommendation."
)

# -----------------------------------------
# Employee Details
# -----------------------------------------

with st.form("expense_form"):

    employee_name = st.text_input("Employee Name")

    employee_id = st.text_input("Employee ID")

    department = st.selectbox(
        "Department",
        [
            "Finance",
            "IT",
            "HR",
            "Sales",
            "Marketing"
        ]
    )

    expense_type = st.selectbox(
        "Expense Type",
        [
            "Hotel",
            "Travel",
            "Meals",
            "Taxi",
            "Office Supplies",
            "Others"
        ]
    )

    amount = st.number_input(
        "Expense Amount",
        min_value=0.0,
        step=1.0
    )

    comments = st.text_area(
        "Comments"
    )

    uploaded_file = st.file_uploader(
        "Upload Receipt",
        type=["pdf", "png", "jpg", "jpeg"]
    )

    submitted = st.form_submit_button("Submit Expense")

# -----------------------------------------
# Submit
# -----------------------------------------

if submitted:

    if uploaded_file is None:
        st.error("Please upload a receipt.")
        st.stop()

    files = {
        "receipt": (
            uploaded_file.name,
            uploaded_file.getvalue()
        )
    }

    data = {
        "employee_name": employee_name,
        "employee_id": employee_id,
        "department": department,
        "expense_type": expense_type,
        "amount": amount,
        "comments": comments
    }

    headers = {
        "x-api-key": Config.API_KEY
    }

    with st.spinner("Analyzing expense..."):

        try:

            api_url = os.getenv("EEM_API_URL", Config.API_URL).rstrip("/")

            response = requests.post(
                f"{api_url}/submit-expense",
                headers=headers,
                data=data,
                files=files,
                timeout=120
            )

            if response.status_code == 200:

                result = response.json()

                st.success("Expense submitted successfully!")
                st.subheader("Employee Guidance")

                # The current API returns the final Employee Agent message
                # as data. Render that message instead of showing escaped
                # JSON/plain text.
                guidance = result.get("data", "")
                if isinstance(guidance, str):
                    render_employee_guidance(guidance)
                else:
                    st.json(guidance)

                with st.expander("View raw API response"):
                    st.json(result)

            else:

                st.error(response.text)

        except Exception as e:

            st.error(str(e))
