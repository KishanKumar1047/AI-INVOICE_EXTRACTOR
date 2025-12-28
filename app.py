from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
import json

# =========================
# CONFIG
# =========================
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "gemini-2.5-flash"
model = genai.GenerativeModel(MODEL_NAME)

# =========================
# GEMINI FUNCTION
# =========================
def get_gemini_response(user_input, image, prompt):
    response = model.generate_content(
        [
            user_input,
            image,
            prompt
        ]
    )
    return response.text


# =========================
# STREAMLIT UI
# =========================
st.set_page_config(
    page_title="Multilanguage Invoice Extractor",
    page_icon="🤖",
    layout="centered"
)

st.header("🤖 Multilanguage Invoice Extractor")

input_text = st.text_input(
    "Optional instruction (e.g., Extract invoice details):",
    key="input_text"
)

uploaded_file = st.file_uploader(
    "Upload an invoice image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_column_width=True)
else:
    image = None

# =========================
# PROMPT
# =========================
system_prompt = """
You are an intelligent invoice extraction system.
Extract all relevant invoice details and return ONLY valid JSON.

Required fields:
- invoice_number
- invoice_date
- vendor_name
- vendor_address
- customer_name
- subtotal
- tax
- total_amount
- currency
- payment_method (if available)

If a field is missing, return null.
Do not add explanations.
"""

# =========================
# SUBMIT
# =========================
if st.button("Extract Invoice"):
    if image is None:
        st.error("Please upload an invoice image.")
    else:
        with st.spinner("Extracting invoice data..."):
            try:
                response = get_gemini_response(
                    input_text,
                    image,
                    system_prompt
                )

                st.subheader("📄 Extracted Invoice Data")

                try:
                    parsed_json = json.loads(response)
                    st.json(parsed_json)
                except json.JSONDecodeError:
                    st.text(response)

            except Exception as e:
                st.error(f"Error: {e}")
