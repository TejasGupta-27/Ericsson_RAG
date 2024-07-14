from VectorDB.client import get_chroma_client
import os 
import google.generativeai as genai
from chromadb.utils import embedding_functions
import uuid
from preprocessing import extract_text_from_pdf, chunk_text
from VectorDB.client import get_chroma_client, get_or_create_collections

from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def store_document_embeddings(document_path, collection_name='document', chunk_size=5, model_name='all-mpnet-base-v2'):
    client = get_chroma_client()
    
    collection = get_or_create_collections(client, collection_name, model_name)
    sentence_trans_ef=embedding_functions.SentenceTransformerEmbeddingFunction(model_name='all-mpnet-base-v2')
    text = extract_text_from_pdf(document_path)
    chunks = chunk_text(text, chunk_size)
    ids = [str(uuid.uuid4()) for _ in range(len(chunks))]
    metadata = [{"document": document_path, "chunk": i} for i in range(len(chunks))]
    
    collection.add(ids=ids, documents=chunks, metadatas=metadata)


def retrieve_documents(query, collection_name='document'):
    client = get_chroma_client()
    sentence_trans_ef=embedding_functions.SentenceTransformerEmbeddingFunction(model_name='all-mpnet-base-v2')
    collection = client.get_collection(name=collection_name)
    results = collection.query(query_texts=[query], n_results=5,)
    return results

def generate_response(query, collection_name='document'):
    documents = retrieve_documents(query, collection_name)
    
    context = ""
    for document in documents["documents"]:
        for i in document :
            context+=i

        
    print (context)  
    prompt = f"User query: {query}\n\nRelevant information:\n{context}\n\nBased on the above information, please provide a detailed response.Dont add on your own anything just stick to the info given and answer the query without any suggestions or recommendations"
    
    response = model.generate_content(prompt)
    return response.text

