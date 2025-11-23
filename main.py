import os
import streamlit as st
from dotenv import load_dotenv

# --- IMPORTS ---
try:
    from langchain_community.document_loaders import CSVLoader
    from langchain_community.vectorstores import FAISS
    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_classic.chains import RetrievalQA
except ImportError as e:
    st.error(f"Import Error: {e}")
    st.stop()
# ----------------

# 1. Load the secret password
load_dotenv()

# --- THE FIX: MANUALLY GRAB THE KEY ---

my_api_key = os.getenv("GOOGLE_API_KEY")
if not my_api_key:
    st.error("🚨 ERROR: I cannot find your GOOGLE_API_KEY! Please make sure your .env file is correct.")
    st.stop()
# --------------------------------------

st.title("🤖 AI Fundamentals Q&A Bot for ML Internships interviews")

# 2. Set up the Brain (Pass the key explicitly!)
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash", 
        temperature=0.2,
        google_api_key=my_api_key  # <--- WE HAND IT THE KEY HERE
    )
    
    instructor_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
except Exception as e:
    st.error(f"Setup Error: {e}")
    st.stop()

# 3. Create the "Knowledge Button"
if st.button("Create Knowledge Base"):
    with st.spinner("Processing..."):
        if os.path.exists("data.csv"):
            loader = CSVLoader(file_path='data.csv', source_column="question")
            data = loader.load()
            
            vectordb = FAISS.from_documents(documents=data, embedding=instructor_embeddings)
            vectordb.save_local("faiss_index")
            st.success("Done! Knowledge Base Created.")
        else:
            st.error("Missing data.csv file!")

# 4. The Question Box
question = st.text_input("Ask a question:")

if question:
    if os.path.exists("faiss_index"):
        vectordb = FAISS.load_local("faiss_index", instructor_embeddings, allow_dangerous_deserialization=True)
        retriever = vectordb.as_retriever()
        
        qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
        
        try:
            response = qa_chain.invoke({"query": question})
            st.write(response["result"])
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Click 'Create Knowledge Base' first.")