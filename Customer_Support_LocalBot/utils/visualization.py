# visualization.py
from pyvis.network import Network
import streamlit as st
import networkx as nx
import tempfile
import os
import uuid
import time
from streamlit.components.v1 import html
import re

def visualize_graph(G, query=None, height=500, width=700):
    """
    Create an interactive visualization of the knowledge graph using pyvis.
    
    Args:
        G: NetworkX graph object
        query: Optional query string to highlight relevant nodes
        height: Height of the visualization
        width: Width of the visualization
    
    Returns:
        HTML string to display in Streamlit
    """
    # Create a pyvis network
    net = Network(height=f"{height}px", width=f"{width}px", notebook=True, directed=False, bgcolor="#ffffff")
    
    # Configure physics for better visualization
    net.barnes_hut(gravity=-5000, central_gravity=0.3, spring_length=150)
    
    # Process query to find relevant terms
    highlighted_nodes = set()
    if query:
        query_terms = set(re.findall(r'\b\w+\b', query.lower()))
        # Find nodes that match query terms
        for node in G.nodes():
            node_terms = set(re.findall(r'\b\w+\b', str(node).lower()))
            if query_terms.intersection(node_terms):
                highlighted_nodes.add(node)
                # Also add immediate neighbors
                for neighbor in G.neighbors(node):
                    highlighted_nodes.add(neighbor)
    
    # Add nodes
    for node in G.nodes():
        # Node styling based on relevance
        if node in highlighted_nodes:
            net.add_node(node, label=node, color="#FF5733", size=25, title=f"Relevant: {node}")
        else:
            net.add_node(node, label=node, color="#97C2FC", size=15, title=node)
    
    # Add edges
    for edge in G.edges():
        if edge[0] in highlighted_nodes and edge[1] in highlighted_nodes:
            # Highlight edges connecting relevant nodes
            net.add_edge(edge[0], edge[1], color="#FF5733", width=2)
        else:
            net.add_edge(edge[0], edge[1], color="#CCCCCC", width=1)
    
    # Generate a unique filename to avoid conflicts
    unique_id = uuid.uuid4().hex
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, f"graph_{unique_id}.html")
    
    try:
        # Save the graph to the unique file
        net.save_graph(file_path)
        
        # Read the HTML content
        with open(file_path, 'r', encoding='utf-8') as f:
            html_string = f.read()
        
        # Add a small delay to ensure file handle is released
        time.sleep(0.1)
        
        # Try to remove the file, but don't fail if we can't
        try:
            os.remove(file_path)
        except Exception as e:
            # Just log the error but continue
            st.error(f"Note: Couldn't remove temp file (this won't affect functionality): {str(e)}")
        
        # Return the HTML content
        return html_string
        
    except Exception as e:
        st.error(f"Error generating graph visualization: {str(e)}")
        return "<p>Unable to generate graph visualization</p>"

def visualize_query_subgraph(G, query, top_k=10):
    """
    Create a visualization focused on the query and its most relevant nodes
    
    Args:
        G: NetworkX graph
        query: The user query
        top_k: Number of nodes to display
    
    Returns:
        HTML component
    """
    if not G or len(G.nodes()) == 0:
        return st.info("Knowledge graph is empty or not available.")
    
    # Extract potential entities from query
    entities = re.findall(r'\b[A-Za-z][a-z]+(?: [A-Za-z][a-z]+)*\b', query)
    
    # Find relevant nodes based on query terms
    query_words = query.lower().split()
    scores = {}
    
    for node in G.nodes():
        node_str = str(node).lower()
        # Calculate relevance score based on word matches
        score = sum(1 for word in query_words if word in node_str)
        if score > 0:
            scores[node] = score
    
    # Get top-k relevant nodes
    relevant_nodes = sorted(scores.keys(), key=lambda x: scores[x], reverse=True)[:top_k]
    
    # Create subgraph with these nodes and their immediate neighbors
    if relevant_nodes:
        subgraph_nodes = set(relevant_nodes)
        for node in relevant_nodes:
            subgraph_nodes.update(G.neighbors(node))
        
        # Create subgraph
        subgraph = G.subgraph(subgraph_nodes)
        html_content = visualize_graph(subgraph, query=query, height=400, width=700)
        return html(html_content, height=400, width=700)
    else:
        # If no relevant nodes found, return a message
        return st.info("No relevant nodes found in knowledge graph for this query.")

def display_graph_visualization(G, query, max_nodes=30):
    """
    Display a graph visualization in Streamlit, with error handling
    
    Args:
        G: NetworkX graph
        query: User query
        max_nodes: Maximum number of nodes to display
    """
    try:
        st.subheader("📊 Knowledge Graph Visualization")
        st.caption("Showing nodes and connections relevant to your query")
        
        if not G or len(G.nodes()) == 0:
            st.info("No knowledge graph data available.")
            return
            
        # Display the visualization
        visualize_query_subgraph(G, query, top_k=max_nodes)
        
    except Exception as e:
        st.error(f"Error displaying graph: {str(e)}")
        st.info("Knowledge graph visualization is unavailable, but other features will continue to work.")