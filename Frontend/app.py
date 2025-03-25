import streamlit as st
import requests
import matplotlib.pyplot as plt
from pyvis.network import Network
import streamlit.components.v1 as components
import tempfile
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BLL.ai_processor import generate_response

API_URL = "http://127.0.0.1:8000/ask"

# Track chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Page layout
st.set_page_config(page_title="🎬 MovieGraphRAG", layout="wide")
st.title("🧠 GraphRAG: Ask anything about movies")

query = st.text_input("What would you like to know?", placeholder="e.g. What is the best action movie from the 90s?")

if st.button("Ask"):
    if not query:
        st.warning("⚠️ Please enter a question!")
    else:
        with st.spinner("Thinking..."):
            response = requests.get(API_URL, params={"query": query}).json()
            answer = generate_response(response, query)
            
            # Visual flags
            show_graph = "<SHOW_GRAPH>" in answer or len(response.get("movies", [])) > 0
            print(show_graph)
                                    
            if show_graph:
                st.markdown("### 🌐 Graph View of Relationships")
                
                # Create and configure network
                net = Network(height="500px", width="100%", bgcolor="#222222", 
                            font_color="white", directed=True)
                
                # Add nodes and edges
                added_nodes = set()  # Track added nodes to avoid duplicates
                
                #print the datatype of response
                print(type(response))
                # Ensure edges are always added, even if nodes already exist
                for m in response["movies"]:
                    movie_id = m["title"].replace(" ", "_")  
                    net.add_node(movie_id, label=m["title"], title="Movie", color="#00ff1e", size=25)

                    # Add actors & edges
                    for actor in m.get("actors", []):
                        actor_id = actor.replace(" ", "_")
                        if actor_id not in added_nodes:
                            net.add_node(actor_id, label=actor, title="Actor", color="#ffa500", size=20)
                            added_nodes.add(actor_id)
                        net.add_edge(actor_id, movie_id, title="ACTED_IN") 

                    # Add directors & edges
                    for director in m.get("directors", []):
                        dir_id = director.replace(" ", "_")
                        if dir_id not in added_nodes:
                            net.add_node(dir_id, label=director, title="Director", color="#ff0000", size=20)
                            added_nodes.add(dir_id)
                        net.add_edge(dir_id, movie_id, title="DIRECTED")  

                # Save and display the graph
                try:
                    # Save graph
                    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.html')
                    net.save_graph(tmp_file.name)
                    tmp_file.close()  # Close before reading

                    # Read & render
                    with open(tmp_file.name, 'r', encoding='utf-8') as f:
                        html = f.read()
                    st.components.v1.html(html, height=500)

                    # Cleanup
                    os.remove(tmp_file.name)
                except Exception as e:
                    st.warning(f"⚠️ Graph visualization failed: {str(e)}")
            
            # Display the answer without visualization tags
            clean_answer = answer.replace("<SHOW_GRAPH>", "")

            st.markdown("### 🤖 AI Response:")
            st.write(clean_answer)

            # Optional: Show raw structured data
            with st.expander("🔎 Show Structured Graph Data"):
                st.json(response)

            # Save to history
            st.session_state.chat_history.append({
                "query": query,
                "answer": answer
            })

# Show chat history
with st.expander("🗂️ Chat History"):
    for chat in reversed(st.session_state.chat_history):
        st.markdown(f"**Q:** {chat['query']}")
        st.markdown(f"**A:** {chat['answer']}")
        st.markdown("---")
