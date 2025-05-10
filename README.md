# PDF Summarizer

A web application built using **Streamlit** for summarizing PDF documents using AI. The app allows users to upload a PDF file, process the file, and generate a concise summary of its contents. The underlying model used for summarization is based on the **DistilBART** transformer model, fine-tuned for text summarization tasks.

## Features

- Upload PDF files for summarization.
- AI-powered text summarization using a pre-trained model.
- Easy-to-use web interface built with Streamlit.

## Installation

To run this app locally, follow the instructions below:

### Requirements

- Python 3.7 or later
- Streamlit
- Hugging Face Transformers
- TensorFlow (or PyTorch, depending on the model backend)

### Steps to Run Locally

1. Clone the repository:

    ```bash
    git clone https://github.com/Indrajit147/pdf-summarizer.git
    cd pdf-summarizer
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

4. Open the provided URL in your web browser to access the app.

## Usage

1. Upload a PDF file using the file uploader widget.
2. Wait for the model to process the file and generate a summary.
3. View the summarized text in the output area.

## Deployment

This app is deployed on [Streamlit Cloud](https://streamlit.io), and can be accessed [here](https://share.streamlit.io/Indrajit147/pdf-summarizer).

## Contributing

Feel free to fork this project and submit pull requests for improvements. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hugging Face for providing the pre-trained summarization model.
- Streamlit for the easy deployment and interactive UI.
- TensorFlow/PyTorch for AI model integration.

