import streamlit as st
import requests
import matplotlib.pyplot as plt
from pyvis.network import Network
import streamlit.components.v1 as components
import tempfile
from BLL.ai_processor import generate_response

API_URL = "http://127.0.0.1:8000/ask"

# Track chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Page layout
st.set_page_config(page_title="🎬 MovieGraphRAG", layout="wide")
st.title("🧠 GraphRAG: Ask Anything About Movies")

query = st.text_input("What would you like to know?", placeholder="e.g. What is the best action movie from the 90s?")

if st.button("Ask"):
    if not query:
        st.warning("⚠️ Please enter a question!")
    else:
        with st.spinner("Thinking..."):
            response = requests.get(API_URL, params={"query": query}).json()
            answer = generate_response(response, query)
            if "graph" in query.lower() or "connection" in query.lower() or "visual" in query.lower():
                answer += "\n<SHOW_GRAPH>"

            # Visual flags
            show_bar = "<SHOW_BAR_CHART>" in answer
            print(show_bar)
            show_graph = "<SHOW_GRAPH>" in answer
            print(show_graph)
            
            if show_bar and "movies" in response:
                top_movies = sorted(response["movies"], key=lambda m: m.get("avg_rating", 0), reverse=True)[:5]
                titles = [m["movie"] for m in top_movies]
                ratings = [m["avg_rating"] for m in top_movies]

                st.markdown("### 📊 Top Rated Movies")
                fig, ax = plt.subplots()
                ax.barh(titles[::-1], ratings[::-1])  # reverse for descending bar chart
                ax.set_xlabel("Avg Rating")
                ax.set_title("Top Rated Movies")
                st.pyplot(fig)

            if show_graph:
                st.markdown("### 🌐 Graph View of Relationships")

                net = Network(height="400px", width="100%", bgcolor="#222", font_color="white")

                for m in response["movies"]:
                    net.add_node(m["id"], label=m["movie"], title="Movie", color="green")
                    for a in m["actors"]:
                        net.add_node(a, label=a, title="Actor", color="orange")
                        net.add_edge(m["id"], a, label="ACTED_IN")
                    for d in m["directors"]:
                        net.add_node(d, label=d, title="Director", color="red")
                        net.add_edge(m["id"], d, label="DIRECTED")
                    for g in m["genres"]:
                        net.add_node(g, label=g, title="Genre", color="blue")
                        net.add_edge(m["id"], g, label="IN_GENRE")

                with tempfile.NamedTemporaryFile("w", delete=False, suffix=".html") as tmp:
                    net.show(tmp.name)
                    components.html(open(tmp.name, "r", encoding="utf-8").read(), height=420)
                    
            # Clean the tags from the answer
            answer = answer.replace("<SHOW_BAR_CHART>", "").replace("<SHOW_GRAPH>", "")

            st.markdown("### 🤖 AI Response:")
            st.write(answer)

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

