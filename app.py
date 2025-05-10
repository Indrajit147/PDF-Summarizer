import os
os.environ["TRANSFORMERS_NO_TF"] = "1"


import streamlit as st
from transformers import pipeline
import PyPDF2

# Set Streamlit page config
st.set_page_config(page_title="PDF Summarizer", layout="wide")

# Sidebar
st.sidebar.title("📄 PDF Summarizer")
uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])

summary_length = st.sidebar.selectbox(
    "Select Summary Length",
    options=["Short (50 words)", "Medium (100 words)", "Long (200+ words)"],
    index=1
)

# Initialize the summarizer
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

summarizer = load_summarizer()

# Main app
st.title("📝 PDF Summarizer App")

if uploaded_file is not None:
    # Read the PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    full_text = ""
    for page in pdf_reader.pages:
        full_text += page.extract_text()

    # Display file info
    st.subheader("📂 Uploaded File Info")
    st.write(f"**File name:** {uploaded_file.name}")
    st.write(f"**Number of pages:** {len(pdf_reader.pages)}")

    # Show full text inside an expander
    with st.expander("🔎 View Extracted Text"):
        st.write(full_text)

    # Determine max length based on user selection
    if "Short" in summary_length:
        max_length = 50
    elif "Medium" in summary_length:
        max_length = 120
    else:
        max_length = 250

    # Summarize the text
    if st.button("🚀 Generate Summary"):
        with st.spinner("Summarizing... Please wait."):
            summary = summarizer(full_text, max_length=max_length, min_length=30, do_sample=False)[0]['summary_text']

        # Show summary inside an expander
        with st.expander("📝 View Summary"):
            st.write(summary)
else:
    st.info("📤 Please upload a PDF file to get started.")

