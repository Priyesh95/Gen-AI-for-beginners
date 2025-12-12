import streamlit as st
import PyPDF2
import io
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate

# Initialize session state for storing data between reruns
if "chunks" not in st.session_state:
    st.session_state.chunks = None
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

st.title("Chatbot")
st.header("My first Chatbot")

# API key input
with st.sidebar:
    api_key = st.text_input("Enter your OpenAI API key", type="password")
    os.environ["OPENAI_API_KEY"] = api_key

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

# Only process if PDF uploaded and API key provided
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
    with st.expander("View Extracted Text"):
        st.text_area("PDF Content", text, height=300)

    # Split into chunks
    with st.spinner("Splitting text into chunks..."):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        chunks = text_splitter.split_text(text)
        st.session_state.chunks = chunks
    
    st.write(f"Split into {len(chunks)} chunks")
    
    # Only create embeddings if API key is provided
    if api_key:
        try:
            # Create embeddings using OpenAI
            with st.spinner("Creating embeddings..."):
                embeddings = OpenAIEmbeddings()
                
            # Create vector store
            with st.spinner("Creating vector store..."):
                vector_store = FAISS.from_texts(chunks, embeddings)
                st.session_state.vector_store = vector_store
            
            st.success("Vector store created successfully!")
        except Exception as e:
            st.error(f"Error creating embeddings: {e}")
    else:
        st.warning("Please provide an OpenAI API key to create embeddings.")

# Chat interface
st.write("### Chat with your document")
user_question = st.text_input("Ask a question about your documents")

if user_question and st.session_state.vector_store and api_key:
    try:
        # Create retrieval chain
        retriever = st.session_state.vector_store.as_retriever(search_kwargs={"k": 3})
        
        # Create prompt template
        template = """Answer the question based only on the following context:
        {context}
        
        Question: {question}
        """
        prompt = ChatPromptTemplate.from_template(template)
        
        # Create model
        model = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0,
        )
        
        # Create chain
        chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | model
            | StrOutputParser()
        )
        
        # Generate response
        with st.spinner("Generating response..."):
            response = chain.invoke(user_question)
        
        st.write("### Response")
        st.write(response)
    except Exception as e:
        st.error(f"Error generating response: {e}")
elif user_question:
    if not api_key:
        st.warning("Please provide an OpenAI API key to use the chat feature.")
    if not st.session_state.vector_store:
        st.warning("Please upload a PDF document first.")
