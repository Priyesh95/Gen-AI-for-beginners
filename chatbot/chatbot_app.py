import streamlit as st
import PyPDF2
import io
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI


OPENAI_API_KEY = "Your OpenAI API Key"


st.title("Chatbot")
st.header("My first Chatbot")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

# Upload PDF files
with st.sidebar:
    st.title("Your Documents")
    pdf_file = st.file_uploader("Upload your documents", type=["pdf"])

# Process uploaded file
if pdf_file is not None:
    # Display file details
    file_details = {
        "Filename": pdf_file.name,
        "File size": f"{pdf_file.size / 1024:.2f} KB"
    }
    st.write("### File Details")
    for key, value in file_details.items():
        st.write(f"**{key}:** {value}")
    
    # Extract text from PDF
    with st.spinner("Extracting text from PDF..."):
        text = extract_text_from_pdf(pdf_file)
    
    # Display extracted text
    st.write("### Extracted Text")
    st.text_area("PDF Content", text, height=400)

# split into chunks
with st.spinner("Splitting text into chunks..."):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_text(text)
st.write("### Text Chunks")
st.write(f"Number of chunks: {len(chunks)}")
st.write(chunks)

# Create embeddings using OpenAI
with st.spinner("Creating embeddings..."):
    embeddings = OpenAIEmbeddings(
        model_name="text-embedding-ada-002",
        api_key=OPENAI_API_KEY
    )
        
# Create vector store
with st.spinner("Creating vector store..."):
    vector_store = FAISS.from_texts(chunks, embeddings)
st.write("### Vector Store")
st.write(vector_store)

# Get user question
user_question = st.text_input("Ask a question about your documents")

# Do a similarity search
with st.spinner("Searching for similar documents..."):
    similar_docs = vector_store.similarity_search(user_question, k=5)
st.write("### Similar Documents")
st.write(similar_docs)

# Create chatbot
chatbot = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    api_key=OPENAI_API_KEY
    temperature=0,
    max_tokens=1000,
)

# Generate response using chatbot
with st.spinner("Generating response..."):
    response = chatbot.generate_text(user_question, search_results=similar_docs)
st.write("### Response")
st.write(response)



        
        
