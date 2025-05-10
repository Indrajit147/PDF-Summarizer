import streamlit as st
from transformers import pipeline
from PyPDF2 import PdfReader

# Load the pre-trained summarizer model from Hugging Face
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def generate_summary(text):
    summary = summarizer(text, max_length=300, min_length=100, do_sample=False)
    return summary[0]['summary_text']

# Streamlit UI setup
st.title("PDF Summarizer")
st.write("Upload your PDF to get a summary!")

# File uploader widget
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Extract text from the uploaded PDF
    text = extract_text_from_pdf(uploaded_file)
    
    # Check if text extraction was successful
    if text.strip():
        # Show original text preview (optional)
        st.subheader("Original Text")
        st.write(text[:1500])  # Display the first 1500 characters of the extracted text
        
        # Generate summary
        summary = generate_summary(text)
        
        # Display the summary
        st.subheader("Summary")
        st.write(summary)
    else:
        st.error("No text could be extracted from the PDF. Please try a different file.")
