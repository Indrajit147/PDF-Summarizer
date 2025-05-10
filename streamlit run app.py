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

def chunk_text(text, max_chunk_length=1000):
    paragraphs = text.split("\n")
    chunks = []
    current_chunk = ""
    for para in paragraphs:
        if len(current_chunk) + len(para) <= max_chunk_length:
            current_chunk += para + "\n"
        else:
            chunks.append(current_chunk)
            current_chunk = para + "\n"
    if current_chunk:
        chunks.append(current_chunk)
    return chunks

def generate_summary(text):
    chunks = chunk_text(text)
    summary = ""
    for chunk in chunks:
        if len(chunk.strip()) == 0:
            continue
        summarized = summarizer(chunk, max_length=300, min_length=100, do_sample=False)
        summary += summarized[0]['summary_text'] + " "
    return summary

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


#streamlit run app.py
