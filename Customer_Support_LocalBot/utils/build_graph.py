# build_graph.py
import streamlit as st
import networkx as nx
import re
from utils.visualization import visualize_graph, visualize_query_subgraph

def build_knowledge_graph(docs):
    """
    Build a knowledge graph from document contents by extracting entities and relationships.
    
    Args:
        docs: List of document objects with page_content attribute
    
    Returns:
        NetworkX graph object
    """
    G = nx.Graph()
    
    for doc in docs:
        # Extract potential entities (starting with capital letters)
        entities = re.findall(r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)*\b', doc.page_content)
        
        # Add nodes and edges
        if len(entities) > 1:
            # Add all entities as nodes
            for entity in entities:
                if not G.has_node(entity):
                    G.add_node(entity, type="entity", count=1)
                else:
                    # Increment count if node already exists
                    G.nodes[entity]["count"] = G.nodes[entity].get("count", 0) + 1
            
            # Connect entities that appear close to each other
            for i in range(len(entities) - 1):
                if entities[i] != entities[i + 1]:  # Avoid self-loops
                    if G.has_edge(entities[i], entities[i + 1]):
                        # Increment weight if edge already exists
                        G[entities[i]][entities[i + 1]]["weight"] = G[entities[i]][entities[i + 1]].get("weight", 1) + 1
                    else:
                        G.add_edge(entities[i], entities[i + 1], weight=1)
    
    # Remove nodes with low connectivity (optional)
    nodes_to_remove = [node for node, degree in dict(G.degree()).items() if degree < 2]
    G.remove_nodes_from(nodes_to_remove)
    
    return G


def retrieve_from_graph(query, G, top_k=5):
    """
    Retrieve relevant information from the knowledge graph based on query.
    
    Args:
        query: User query string
        G: NetworkX graph object
        top_k: Number of top results to return
    
    Returns:
        List of relevant nodes/content
    """
    # Debug log
    st.write(f"🔎 Searching GraphRAG for: {query}")

    # Convert query into words to match knowledge graph nodes
    query_words = query.lower().split()
    matched_nodes = [node for node in G.nodes if any(word in node.lower() for word in query_words)]
    
    # Get related nodes
    if matched_nodes:
        # Track all related nodes
        related_nodes = set()
        
        # Get first-degree connections
        for node in matched_nodes:
            related_nodes.update(G.neighbors(node))
            related_nodes.add(node)  # Include the matched node itself
        
        # Convert to list and sort by node degree (connection importance)
        sorted_nodes = sorted(related_nodes, key=lambda x: G.degree(x), reverse=True)[:top_k]
        
        # Display visualization in a collapsible section
        with st.expander("📊 Knowledge Graph Visualization", expanded=False):
            st.write("Showing nodes related to your query:")
            
            # Create subgraph for visualization
            query_subgraph = visualize_query_subgraph(G, query, top_k=top_k)
            
            # Display export button
            if st.button("Export Graph"):
                # Create full graph visualization for download
                full_vis = visualize_graph(G, query=None)
                st.download_button(
                    label="Download Graph HTML",
                    data=full_vis,
                    file_name="knowledge_graph.html",
                    mime="text/html"
                )
        
        # Debug info
        st.write(f"🟢 GraphRAG Matched Nodes: {matched_nodes}")
        st.write(f"🟢 GraphRAG Retrieved Related Nodes: {sorted_nodes}")
        
        return sorted_nodes
    
    st.write(f"❌ No graph results found for: {query}")
    return []