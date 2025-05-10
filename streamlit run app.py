import os
os.environ["TRANSFORMERS_NO_TF"] = "1"


import streamlit as st
from transformers import pipeline
import PyPDF2

# Initialize summarization pipeline
st.title("📄 PDF Summarizer App")

st.write("""
Welcome to the **PDF Summarizer App**!  
Upload a PDF file and get an AI-generated summary in seconds.  
_Built with Streamlit + Hugging Face Transformers._
""")

# Load summarizer with caching
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

summarizer = load_summarizer()

# Upload the PDF
uploaded_file = st.file_uploader("👉 Upload your PDF file here", type=['pdf'])


if uploaded_file is not None:
    try:
        # Extract text from PDF
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page_num, page in enumerate(pdf_reader.pages):
            page_text = page.extract_text()
            if page_text:
                text += page_text

        # Show preview of extracted text
        if text:
            st.subheader("📖 Extracted Text Preview (first 1000 characters):")
            st.text(text[:1000] + "..." if len(text) > 1000 else text)

            # Button to summarize
            if st.button("🚀 Generate Summary"):
                with st.spinner("AI is summarizing your document..."):
                    # Truncate if text is too long (model limit ~1024 tokens)
                    if len(text) > 3000:
                        text = text[:3000]

                    summary = summarizer(
                        text,
                        max_length=200,
                        min_length=50,
                        do_sample=False
                    )[0]['summary_text']

                st.subheader("📝 Summary:")
                st.success(summary)
        else:
            st.warning("⚠️ No text could be extracted from the uploaded PDF.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
