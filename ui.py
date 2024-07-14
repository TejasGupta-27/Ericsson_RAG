import streamlit as st
from rag_pipeline import generate_response, store_document_embeddings
from preprocessing import extract_text_from_pdf, chunk_text

# Page title and configuration
st.set_page_config(page_title="Ericsson Chat Interface", page_icon="🤖")

# Initialize session state for chat history and uploaded file state
if 'history' not in st.session_state:
    st.session_state.history = []

if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None

# Function to display chat messages in a chat message container style
def display_chat_messages(messages):
    for idx, message in enumerate(messages):
        if 'role' in message and 'content' in message:
            if message['role'] == 'user':
                st.info(f"You: {message['content']}")
            elif message['role'] == 'bot':
                st.success(f"Bot: {message['content']}")

# Sidebar for File Upload and Embeddings
with st.sidebar:
    st.image('ericsson_logo.png', use_column_width=True)  # Replace with actual path to your logo image
    st.title('Ericsson Chat Interface')
    st.markdown('📖 Learn how to build this app in this [blog](https://blog.streamlit.io/how-to-build-an-llm-powered-chatbot-with-streamlit/)!')

    # File uploader for PDFs
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
    if uploaded_file is not None:
        with open(f"data/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("File uploaded successfully!")

        # Update session state with uploaded file
        st.session_state.uploaded_file = f"data/{uploaded_file.name}"

# Automatically process and store embeddings when a file is uploaded
if st.session_state.uploaded_file:
    store_document_embeddings(st.session_state.uploaded_file, chunk_size=5)
    st.success("Document processed and embeddings stored successfully!")
    # Reset uploaded file state to None to prevent automatic re-processing
    st.session_state.uploaded_file = None

# Container for the conversation
conversation_area = st.empty()

# User input for query (moved to sidebar)
with st.sidebar:
    query = st.text_input('Enter your query:', key='query_input')

    # Handle user query submission
    if st.button('Send'):
        if query:
            # Add user query to history
            st.session_state.history.append({'role': 'user', 'content': query})
            # Generate bot response
            response = generate_response(query)
            # Add bot response to history
            st.session_state.history.append({'role': 'bot', 'content': response})
        else:
            st.warning("Please enter a query.")

# Display updated chat messages
display_chat_messages(st.session_state.history)
