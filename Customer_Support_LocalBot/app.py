#app.py
import streamlit as st
import requests
import json
from utils.retriever_pipeline import retrieve_documents
from utils.doc_handler import process_documents
from sentence_transformers import CrossEncoder
import torch
import os
from dotenv import load_dotenv, find_dotenv
from utils.visualization import visualize_graph, visualize_query_subgraph
import time  

torch.classes.__path__ = [os.path.join(torch.__path__[0], torch.classes.__file__)]  # Fix for torch classes not found error
load_dotenv(find_dotenv())  # Loads .env file contents into the application based on key-value pairs defined therein, making them accessible via 'os' module functions like os.getenv().

OLLAMA_BASE_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434")
OLLAMA_API_URL = f"{OLLAMA_BASE_URL}/api/generate"
MODEL= os.getenv("MODEL", "deepseek-r1:7b")                                                      #Make sure you have it installed in ollama
EMBEDDINGS_MODEL = "nomic-embed-text:latest"
CROSS_ENCODER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

device = "cuda" if torch.cuda.is_available() else "cpu"
# 🚀 Initialize Cross-Encoder (Reranker) at the global level 
reranker = None                                                        
try:
    reranker = CrossEncoder(CROSS_ENCODER_MODEL, device=device)
except Exception as e:
    st.error(f"Failed to load CrossEncoder model: {str(e)}")


# ✅ Streamlit configuration
st.set_page_config(page_title="Local Customer Bot Assistant", layout="wide")      

# Custom CSS
st.markdown("""
    <style>
        .stApp { background-color: #f4f4f9; }
        h1 { color: #00FF99; text-align: center; }
        .stChatMessage { border-radius: 10px; padding: 10px; margin: 10px 0; }
        .stChatMessage.user { background-color: #e8f0fe; }
        .stChatMessage.assistant { background-color: #d1e7dd; }
        .stButton>button { background-color: #00AAFF; color: white; }
    </style>
""", unsafe_allow_html=True)


# Manage Session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "retrieval_pipeline" not in st.session_state:
    st.session_state.retrieval_pipeline = None
if "rag_enabled" not in st.session_state:
    st.session_state.rag_enabled = False
if "documents_loaded" not in st.session_state:
    st.session_state.documents_loaded = False

# 📁 Sidebar
with st.sidebar:                                                                       
    st.header("📁 Document Management")
    uploaded_files = st.file_uploader(
        "Upload documents (PDF/DOCX/TXT)",
        type=["pdf", "docx", "txt"],
        accept_multiple_files=True
    )
    
    if uploaded_files and not st.session_state.documents_loaded:
        with st.spinner("Processing documents..."):
            process_documents(uploaded_files,reranker,EMBEDDINGS_MODEL, OLLAMA_BASE_URL)
            st.success("Documents processed!")
    
    st.markdown("---")
    st.header("⚙️ RAG Settings")
    
    st.session_state.rag_enabled = st.checkbox("Enable RAG", value=True)
    st.session_state.enable_hyde = st.checkbox("Enable HyDE", value=True)
    st.session_state.enable_reranking = st.checkbox("Enable Neural Reranking", value=True)
    st.session_state.enable_graph_rag = st.checkbox("Enable GraphRAG", value=True)
    st.session_state.temperature = st.slider("Temperature", 0.0, 1.0, 0.3, 0.05)
    st.session_state.max_contexts = st.slider("Max Contexts", 1, 5, 3)
    

    st.markdown("---")
    st.header("📊 Graph Visualization")
    st.session_state.show_graph = st.checkbox("Show Graph Visualization", value=True)
    st.session_state.graph_height = st.slider("Graph Height", 300, 800, 500, 50)
    st.session_state.graph_width = st.slider("Graph Width", 400, 1000, 700, 50)
    st.session_state.max_graph_nodes = st.slider("Max Graph Nodes", 10, 100, 30, 5)

    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

    # 🚀 Footer (Bottom Right in Sidebar) For some Credits :)
    st.sidebar.markdown("""
        <div style="position: absolute; top: 20px; right: 10px; font-size: 12px; color: gray;">
            <b>Developed by:</b> N Sai Akhil - Adapted by Adriano Dias
        </div>
    """, unsafe_allow_html=True)

# 💬 Chat Interface
st.title("🤖 Hello, I am your customer assistant bot !")
st.caption("Advanced RAG System with GraphRAG, Hybrid Retrieval, Neural Reranking and Chat History")

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about your documents..."):
    chat_history = "\n".join([msg["content"] for msg in st.session_state.messages[-5:]])
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Create a separate container for the graph visualization OUTSIDE the chat message
    if st.session_state.show_graph and st.session_state.enable_graph_rag and st.session_state.rag_enabled and st.session_state.retrieval_pipeline:
        graph_container = st.container()
        with graph_container:
            try:
                # Get the knowledge graph
                G = st.session_state.retrieval_pipeline["knowledge_graph"]
                
                # Use the safer display function with error handling
                from utils.visualization import display_graph_visualization
                
                try:
                    display_graph_visualization(
                        G, 
                        prompt, 
                        max_nodes=st.session_state.max_graph_nodes
                    )
                except Exception as e:
                    st.error(f"Graph visualization error: {str(e)}")
            except Exception as e:
                st.error(f"Graph error: {str(e)}")
    
    # 🚀 Build context
    context = ""
    if st.session_state.rag_enabled and st.session_state.retrieval_pipeline:
        try:
            # Retrieve documents
            docs = retrieve_documents(prompt, OLLAMA_API_URL, MODEL, chat_history)
            context = "\n".join(
                f"[Source {i+1}]: {doc.page_content}" 
                for i, doc in enumerate(docs)
            )
        except Exception as e:
            st.error(f"Retrieval error: {str(e)}")
    
    # Generate response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        # 🚀 Structured Prompt
        system_prompt = f"""Use the chat history to maintain context:
            Chat History:
            {chat_history}

            Analyze the question and context through these steps:
            1. Identify key entities and relationships
            2. Check for contradictions between sources
            3. Synthesize information from multiple contexts
            4. Formulate a structured response

            Context:
            {context}

            Question: {prompt}
            Answer:"""
        
        # Let the user know we're generating a response
        response_placeholder.markdown("*Generating response...*")
        
        start_time = time.time()
        
        # Stream response
        response = requests.post(
            OLLAMA_API_URL,
            json={
                "model": MODEL,
                "prompt": system_prompt,
                "stream": True,
                "options": {
                    "temperature": st.session_state.temperature,
                    "num_ctx": 4096
                }
            },
            stream=True
        )
        
        try:
            for line in response.iter_lines():
                if line:
                    data = json.loads(line.decode())
                    token = data.get("response", "")
                    full_response += token
                    response_placeholder.markdown(full_response + "▌")
                    
                    # Stop if we detect the end token
                    if data.get("done", False):
                        break
            
            # Calculate generation time
            generation_time = time.time() - start_time
            
            # Display final response without the cursor
            response_placeholder.markdown(full_response)
            
            # Save response to session state
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Generation error: {str(e)}")
            st.session_state.messages.append({"role": "assistant", "content": "Sorry, I encountered an error."})
        
    # Display timing information AFTER the chat message (outside the chat_message context)
    st.caption(f"⏱️ Response generated in {generation_time:.2f} seconds")