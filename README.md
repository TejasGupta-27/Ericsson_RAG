# RAG

RAG is a Streamlit-based application that allows users to interact with document databases using a conversational interface. The application supports uploading documents, extracting embeddings for efficient querying, and generating responses in real-time.

## Features

- **Document Upload:** Supports PDF, DOCX, and TXT file uploads.
- **Embedding Storage:** Automatically processes uploaded documents and stores embeddings for efficient querying.
- **Real-Time Conversational Interface:** Allows users to query the document database and receive responses in a streaming, conversational manner.
- **Session Management:** Maintains chat history and handles file uploads within the session.

## Installation

### Prerequisites

- Python 3.8 or higher
- Virtual environment tool (optional but recommended)

### Setup

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/TejasGupta-27/RAG.git
    cd RAG
    ```

2. **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application:**
    ```bash
    streamlit run ui.py
    ```

5. **Access the Interface:**
   Open your web browser and go to `http://localhost:8501`.

## Usage

### Uploading Documents

1. **Navigate to the Sidebar:**
   - Click the "Browse files" button under the "Upload a File" section.
   - Select your PDF, DOCX, or TXT file.

2. **Automatic Processing:**
   - The document will be automatically processed, and embeddings will be stored.

3. **Querying the Database:**
   - Enter your query in the text input field in the sidebar.
   - Click "Send" to submit your query.
   - The bot will respond in the main chat area with relevant information extracted from the uploaded documents.

### Viewing Chat History

- The chat history will be displayed in the main conversation area, showing both user queries and bot responses.

## Project Structure

```plaintext
├── data/                          # Directory for temporary files
│   └── temp/                      # Temporary storage for uploaded files
├── preprocessing.py               # Script for document text extraction and chunking
├── rag_pipeline.py                # Script for generating responses and storing embeddings
├── ui.py                          # Main Streamlit application
├── logo.png                       # Logo image displayed in the sidebar
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
Future Enhancements

    Enhanced Query Expansion: Implement more advanced query expansion techniques to improve document retrieval accuracy.
    Multi-Language Support: Add support for processing and querying documents in multiple languages.
    User Authentication: Introduce user authentication to manage document access and interaction history.
