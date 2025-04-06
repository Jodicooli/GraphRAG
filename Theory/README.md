# Graph RAG

This README file contains theory aspects as well as practical examples about GraphRAG and its usage.

## Table of Contents

1. [Introduction](#introduction)
2. [Background &amp; History](#background--history)
3. [Key Concepts &amp; Theoretical Foundations](#key-concepts--theoretical-foundations)
4. [Applications &amp; Use Cases](#applications--use-cases)
5. [Exploring Graph RAG in Practice](#exploring-graph-rag-in-practice)
6. [To be defined](#to be defined)
7. [Comparing Graph RAG with Alternative Approaches](#comparing-graph-rag-with-alternative-approaches)
8. [Conclusion and Next Steps](#conclusion-and-next-steps)
9. [References](#references)

---

## 1. Introduction

Retrieval-Augmented Generation (RAG) is a method that improves AI responses by combining a search system with a generative model. However, RAG has limitations in understanding complex relationships between concepts.

Knowledge graphs help solve this issue by structuring information as connected entities and relationships. Graph RAG builds on this idea by integrating knowledge graphs into RAG, leading to more accurate and context-aware responses.

This project explores how Graph RAG enhances AI retrieval and generation, its applications, and how to build a custom knowledge graph for better AI understanding.

![Data Exchange in GraphRAG](images/image.png)

## 2. Background & History

### Evolution of AI-Assisted Retrieval Systems

AI-assisted recovery systems have evolved significantly over time to become smarter and more precise. ( *Evolution Of AI In Information Retrieval | Restackio* , s. d.)

* Traditional search engines (1990s - 2000s): These use keyword search and page ranking algorithms (such as PageRank). Their main drawback is that they don't really understand the context of queries, which can lead to irrelevant results. ( *Définition du PageRank - Agence SEO.fr* , 2024)
* NLP-based search models (2000s - 2010s): Models such as TF-IDF and Word2Vec have been developed to better understand the meaning of words and their importance in context. TF-IDF measures word relevance based on frequency and distribution, while Word2Vec captures semantic relationships by representing words as vectors. However, these models do not take context into account. A word will always have the same meaning, regardless of the surrounding words in the sentence. (Fokou, 2019)
* Transformers and pre-trained models (2017 - Present): The introduction of Transformers (e.g. BERT, RoBERTa) has revolutionized search systems by enabling better understanding of complete sentences. These models use attention mechanisms to analyze all the dependencies between words in a sentence, enabling them to capture the overall context. Unlike previous models, they give different meanings to words depending on context, resulting in a better understanding of sentences and more accurate results. (Fokou, 2019)
* RAG (Retrieval-Augmented Generation) (2020 - Present): Introduced by Facebook AI in 2020, RAG combines an intelligent search engine with a generative model to produce answers based on relevant documents. This approach significantly improves the accuracy of answers by using up-to-date information from external sources, while generating coherent, contextually appropriate texts. (Merritt, 2025)
* GraphRAG (2024 - Present): GraphRAG is an enhancement to RAG that uses graphs to organize and link information. Instead of just using conventional databases. This makes it easier to understand the relationships between concepts, and improves the accuracy of answers, particularly for complex questions requiring several stages of reasoning. ( *Welcome - GraphRAG* , s. d.-b)

### The Development of RAG and Its Limitations

The main idea behind RAG is to combine the advantages of search systems (contextual accuracy) with those of generative models (fluidity and creativity).

Limitations of RAG :

* The quality of answers depends on the quality and relevance of the documents retrieved. (Harsh & Harsh, 2024)
* RAG doesn't really understand the complex relationships between concepts. For example, it might not make the connection between “CEO” and “company director” without having seen these terms used together in a document. (Harsh & Harsh, 2024)
* The generative model can introduce inconsistencies if documents are contradictory. (Harsh & Harsh, 2024)

### How Knowledge Graphs Enhance AI Understanding

Knowledge Graphs provide a solution to the limitations of RAG by providing a semantic and relational structure to information.

* Unlike a traditional database, a Knowledge Graph links entities (nodes) by relationships (edges). For example

  * Entities: “Steve Jobs”, “Apple Inc.”, “iPhone”.
  * Relationships: “founded”, “created”.

  This enables AI to understand not only words, but also the relationships between them.
* A Knowledge Graph helps AI distinguish between similar concepts using relational context. For example, it can differentiate “Apple” (company) from “apple” (fruit) based on relationships (“founded” vs. “part of”).
* AI can use relationships to deduce new information. For example, if “Steve Jobs founded Apple” and “Apple created the iPhone”, the AI can deduce that “Steve Jobs helped create the iPhone”.
* By combining GraphRAG with RAG, the Knowledge Graph is used to augment queries by providing relevant context. This makes it possible to ask more precise questions and obtain more relevant answers.

## 3. Key Concepts & Theoretical Foundations

### Fundamentals of Retrieval-Augmented Generation (RAG), Knowledge Graphs, and Graph RAG

RAG combines **information retrieval** and **text generation**, allowing AI to fetch relevant knowledge before constructing responses.

Graph RAG enhances this by structuring information in a **network of interconnected concepts**, improving contextual understanding.

### How RAG Works: Retrieval and Generation

- **Retrieval Phase**: The system searches a knowledge base for relevant documents before generating a response.
- **Generation Phase**: It synthesizes the retrieved knowledge to produce a clear and contextually relevant answer.

### The Role of Graphs in AI and Knowledge Representation

- Graph RAG represents information as a **network of linked concepts** rather than isolated documents.
- For example, in understanding *electric cars*:

  - "Electric car" → "Battery"
  - "Battery" → "Lithium"
  - "Lithium" → "Mining industry"
- These connections improve knowledge structuring and response accuracy.

### Advantages and Challenges of Using Graph RAG

#### **Advantages**

**More accurate responses** – Finds the most relevant information dynamically.

**Better contextual understanding** – Connects related concepts for improved comprehension.

**Verifiable answers** – Can cite sources, enhancing reliability.

#### **Challenges**

**Managing large data volumes** – Organizing and retrieving vast amounts of information efficiently.

**Keeping knowledge up to date** – Regular updates are required to maintain accuracy.

**Ensuring quality relationships** – Conceptual connections must remain relevant and meaningful.

### 3.1 What is RAG ?

Retrieval-Augmented Generation (RAG) is an approach that enhances traditional generative models by incorporating a retrieval step. Instead of relying solely on the training data, RAG systems actively search for relevant external information, which helps generate responses that are more accurate, current, and grounded in real-world data.

**Two-Step Process:**

1. **Retrieval:** When a query is made, the system first searches through a large repository of documents or data to fetch the most relevant pieces of information.
2. **Generation:** The generative model then uses this retrieved context to produce a response that is not only coherent but also enriched with factual data from the external sources.

**Addressing Limitations of Standalone Generative Models:**

Traditional language models may “hallucinate” details or provide outdated responses because they rely solely on static training data. RAG overcomes this limitation by dynamically retrieving the most pertinent and up-to-date information, which helps improve the accuracy and reliability of the output.

**Enhancements and Further Insights (from IBM Research):**

IBM Research further elaborates on this concept by emphasizing that RAG combines neural retrieval techniques with generative models to create a more robust and flexible framework. According to their research, this method allows the system to:

* **Adapt to Domain-Specific Tasks:** By fine-tuning both the retrieval and generation components, RAG can be tailored to meet the demands of specialized applications, ensuring higher performance and relevance in particular domains (Martineau, 2024).
* **Improve Responsiveness:** The retrieval component can quickly sift through extensive datasets using advanced indexing methods, enabling the model to promptly incorporate the latest information (Martineau, 2024).
* **Mitigate Knowledge Decay:** As models age, their training data can become outdated. RAG addresses this by continuously pulling in fresh, external information during the generation process, thereby maintaining relevance over time (Martineau, 2024).

### 3.2 The Role of Graphs in AI and Knowledge Representation

Graphs play a crucial role in knowledge representation, especially in the context of AI. They provide a flexible and intuitive way to structure and visualize complex relationships between entities. In AI, graphs are used to represent a wide range of data, from knowledge graphs and semantic networks to social networks and biological data.

**Why Graphs Matter in AI:**

1. **Representation of Relationships:** Graphs naturally model relationships between entities, where nodes represent entities (e.g., people, places, concepts) and edges represent relationships (e.g., "is related to", "is part of"). This makes graphs highly suitable for tasks such as question answering, reasoning, and information retrieval.
2. **Contextual Understanding:** Graph-based representations enable AI models to not only access facts but also to understand the context in which these facts exist. This helps AI systems answer more sophisticated queries by understanding how different pieces of information relate to each other.
3. **Semantic Reasoning:** Graphs enable semantic reasoning, allowing AI systems to infer new facts or relationships that are not explicitly stated, enhancing the system's ability to handle ambiguous or incomplete information.

**Knowledge Graphs in AI:**
In AI, knowledge graphs are particularly important because they provide structured data that can be queried and reasoned over. By storing facts in a graph format, systems can quickly retrieve relevant data and infer new insights. For instance, a knowledge graph about medical conditions can help a diagnostic AI model infer potential diagnoses based on symptoms and historical data.

### 3.3 Advantages and Challenges of Using Graph RAG

Graph-based RAG, which integrates retrieval-augmented generation with graph-based knowledge representation, offers a variety of benefits but also presents certain challenges.

**Advantages of Graph RAG:**

1. **Improved Accuracy and Relevance:**

   * By combining the retrieval process with graph-based data, Graph RAG can provide responses that are not only grounded in real-world data but also contextually rich. The relationships between entities stored in a graph allow the generative model to produce more accurate and relevant answers.
2. **Better Handling of Complex Queries:**

   * Complex queries that involve multiple relationships or require reasoning across different data points can benefit significantly from graph-based retrieval. The structure of the graph helps the retrieval process find more comprehensive and interconnected information, which can then be used by the generator to form a more detailed response.
3. **Dynamic and Adaptive Responses:**

   * Just like RAG systems, Graph RAG benefits from dynamic retrieval. However, in this case, the retrieval step is guided by the graph's inherent structure, allowing the system to adapt more flexibly to different domains. This ensures that even domain-specific queries can be answered with high accuracy.
4. **Scalability:**

   * As knowledge grows, so does the graph, allowing the model to scale seamlessly. By continuously adding new data to the graph, the system can maintain up-to-date knowledge without the need for re-training the generative model.

**Challenges of Graph RAG:**

1. **Complexity of Graph Construction:**

   * Constructing and maintaining high-quality knowledge graphs can be challenging, especially when dealing with large, unstructured data sources. It requires careful data modeling, validation, and continuous updates to ensure the graph remains accurate and comprehensive.
2. **Integration Complexity:**

   * Integrating graph-based retrieval with generative models can be technically challenging. The generative model must be capable of interpreting the graph's structure and using it to inform its responses. This often requires custom architectures and additional preprocessing steps to align the retrieved data with the model's input format.
3. **Computational Overhead:**

   * The retrieval process in Graph RAG often requires sophisticated algorithms to search and traverse the graph, especially as the size of the graph grows. This can introduce computational overhead, making the system slower compared to traditional RAG models. Optimizing graph retrieval methods is crucial to ensure real-time performance.
4. **Handling Ambiguity and Uncertainty:**

   * Graph-based systems may struggle with ambiguous relationships or incomplete graphs. If the graph lacks sufficient connections or data points, the retrieval process may miss crucial context, resulting in less accurate or incomplete answers.

## 4. Applications & Use Cases

### Why use GraphRAG

As already explained in the chapters above GraphRAG is an enhanced version of Retrieval-Augmented Generation that integrates knowledge graphs into the retrieval process. While traditional RAG relies only on vector similarity to find relevant information, GraphRAG extracts entities and relationships, creating a structured semantic network of knowledge (SivaParam, 2024).

#### But why does this matter?

- Better Contextual Understanding – Instead of retrieving disconnected documents, GraphRAG captures the meaning behind words and their relationships, leading to more accurate results (Bouchard, 2024).
- Multi-Hop Reasoning – Complex queries often require linking multiple pieces of information (e.g., “How does Theory A relate to Research B?”). GraphRAG enables relationship-based retrieval, reducing hallucinations (Bouchard, 2024).
- Improved Query Handling – If users ask high-level or meta-questions (e.g., “How many research papers on RAG were published in 2023?”), GraphRAG can navigate the data structure more effectively than traditional methods (Bouchard, 2024).
- Optimized for Structured Data – If your dataset already contains interconnected information (e.g., citations in academic papers, linked legal documents, or organizational knowledge bases), GraphRAG outperforms standard RAG (Bouchard, 2024).

#### When should you use GraphRAG?

- When your data is **naturally structured as a graph** (e.g., legal documents, research papers, corporate knowledge bases) (Bouchard, 2024).
- When queries require **deep reasoning** (e.g., multi-document comparisons, cause-and-effect relationships) (Bouchard, 2024).
- When reducing hallucinations is critical, and factual consistency is a priority (Bouchard, 2024).
- Your knowledge base is large and constantly evolving (e.g., dynamic research data, market trends) (Korland, 2025).
- Your domain benefits from **structured connections between entities** (e.g., scientific citations, regulatory dependencies) (Korland, 2025).

#### When to avoid GraphRAG?

- Your data consists of **independent documents without meaningful relationships** (Bouchard, 2024).
- GraphRAG requires more computation and processing time, so if your use case is simple, it may not be necessary (Bouchard, 2024).
- You need fast, real-time responses (GraphRAG can be slower than basic RAG) (Korland, 2025).
- You **lack structured data** or the resources to build a knowledge graph (Korland, 2025).

### Examples of sectors where GraphRAG works well

Key sectors where GraphRAG proves valuable include:

#### Healthcare

- **Medical Diagnosis**: Assists healthcare professionals by integrating patient histories, clinical data, and medical literature for precise diagnostic suggestions (Sparkbit, 2025).
- **Drug Research**: Identifies complex relationships between genes, proteins, and compounds, accelerating biomedical discoveries (Sparkbit, 2025).
- **Treatment Planning**: Personalizes care by analyzing genetic data, medical history, and research to recommend the most effective treatments (Sparkbit, 2025).

#### Finance

- **Fraud Detection**: Maps connections between transactions and accounts to identify anomalies and hidden fraudulent activities (Sparkbit, 2025).
- **Risk Management**: Assesses market trends, economic indicators, and financial statements for more accurate predictions (Sparkbit, 2025).
- **Regulatory Compliance**: Helps financial institutions navigate regulations by structuring legal data and transaction records (Sparkbit, 2025).

#### Customer Service

- **Query Understanding & Ticketing**: Improves multi-step query resolution by linking FAQs, troubleshooting guides, and user history (Sparkbit, 2025).
- **Personalization**: Enhances customer experience by analyzing past interactions and preferences to deliver tailored responses (Sparkbit, 2025).

Across these sectors, GraphRAG acts as an assistive tool for human operators, enabling better decision-making and problem-solving through enhanced AI-driven insights.

### Concrete examples

#### Fraud Detection - Paysafe

Example: **Paysafe**, a payment processing company, uses Oracle’s graph technology to detect fraud.

How GraphRAG Helps:

- Finds hidden connections between fraudulent transactions (Hafeez, 2024)
- Speeds up fraud detection from hours to seconds (Hafeez, 2024)
- Prevents cybercrime by flagging unusual transaction patterns (Hafeez, 2024)

#### Healthcare - Precina

Precina Health uses GraphRAG and Memgraph to improve care for patients with Type 2 diabetes. Their system, called P3C (Provider-Patient CoPilot), helps doctors make better treatment decisions by combining medical records with behavioral and social data. This approach has led to significant improvements, with patients lowering their HbA1C levels by 1% per month, a much faster rate than usual (Bryan, n.d.).

P3C works by integrating real-time patient inputs, such as insulin levels, lifestyle factors, and even personal challenges like transportation issues or stress. The system connects these data points to find patterns and predict potential health risks. This allows providers to make informed decisions tailored to each patient’s needs, improving both medical outcomes and overall quality of care (Bryan, n.d.).

## 5. Exploring Graph RAG in practice

**Folder structure**
To reflect the different approaches and experiments, our project is organized into multiple self-contained folders, each representing a specific implementation:

- Each folder contains all relevant code, configurations, and examples.
- Each folder also includes its own README file with:

  - Setup & installation instructions
  - Description of the architecture and use case
  - Tool-specific documentation and known issues

This makes it easy to test, compare, or reuse each GraphRAG implementation independently.

**Documentation structure**
Where needed, we also include a documentation/ folder inside the project. This contains:

- Technology-specific guides (e.g., README.neo4j.md, README.faiss.md, README.streamlit.md)
- Installation steps
- Tool advantages/disadvantages
- Alternatives and relevant examples

This helps you understand not just how the tools were used, but why they were chosen.

### 5.1 Creating your own GraphRAG application

Creating your own GraphRAG system — whether through lightweight tools like the graphrag library or full-stack, custom-built architectures — offers a powerful way to experiment, learn, and deliver real value with retrieval-augmented generation and knowledge graphs.

This section outlines both the benefits and downsides of building GraphRAG systems from scratch or via tooling, and how our project was structured around real use cases.

If you want to discover what GraphRAG application we made you can check out the following two fodlers:

- **/Custom_GraphRAG_Application**
- **/GraphRAG_Library**
- **/Customer_Support_Bot**
- **/Employees_Slack_Bot**

#### Benefits of custom GraphRAG implementation

- **Full control and flexibility**
  Custom implementations allow you to define exactly how your system retrieves, links, and generates information. You can tune everything: the graph schema, the retrieval strategy, the AI model, and even the UI.
- **Tailored for your domain**
  Different domains (healthcare, legal, customer support, etc.) benefit from unique data structures. With your own implementation, you can model domain-specific relationships and customize AI prompts accordingly.
- **Integrate with existing systems**
  Custom GraphRAG systems can connect to company databases (e.g., SQL, Neo4j, APIs), enabling use in real-world enterprise settings — something pre-packaged solutions often can’t do.
- **Improve explainability & debugging**
  Having full visibility into each component (retrieval, graph traversal, generation) helps with performance tuning, debugging, and transparency — especially critical for high-stakes domains.

#### Downsides and limitations

- **Higher complexity**
  Building everything from scratch means handling APIs, infrastructure, data transformation, and model coordination. It takes more effort to get it all working seamlessly.
- **Maintenance Overhead**
  Custom pipelines need ongoing care: updating graph data, retraining embeddings, and refactoring as technologies evolve.
- **Steeper Learning Curve**
  Beginners might find it overwhelming to manage all layers — from Neo4j queries to LLM prompt tuning and UI deployment.
- **Slower to Build**
  Compared to libraries like graphrag, full custom systems are slower to get running — especially when integrating multiple components (FAISS, Neo4j, LLMs, UIs).

#### Conclusion on building a custom GraphRAG system

Creating our own GraphRAG system was a rewarding but time-consuming process. While the end result allowed us to build a powerful, flexible AI assistant, the path to get there came with several challenges.

**It's more time-consuming than expected**
Despite modular design, it took several days until all the parts (retrieval, graph queries, LLM reasoning, UI, and APIs) were integrated and working together properly.

**Prompt engineering is a real challenge**
Designing the right AI prompt for responses was much harder than we thought. We tested and iterated through dozens of prompt variations before we achieved something acceptable. Small changes in phrasing had major effects on the model's output.

**LLMs can be expensive**
Using APIs like OpenAI (especially GPT-4) quickly became expensive during testing and development. That’s why we explored local LLMs like Ollama with Llama3, which are free and easy to run locally — but harder to deploy in production environments.

**Full customization is a major advantage**
A key benefit of building your own system is that you can customize everything — the knowledge structure, graph design, LLM behavior, prompt templates, and even UI logic. This level of control is essential in real-world applications.

**Graph databases have a steep learning curve**
Neo4j and graph querying (Cypher language) are extremely powerful, but not beginner-friendly. Understanding how to model relationships and traverse the graph took time, experimentation, and debugging.

**Strong coding skills are required**
Implementing a working system from scratch — especially one that coordinates vector search, graph DBs, and LLMs — requires good programming knowledge in areas like backend development, APIs, and LLM.

**Changing the database caused major setbacks**
At one point, we switched the underlying graph database structure. This required rebuilding the schema, rewriting queries, and adjusting prompts — which led to lost time and new bugs. The prompt logic was especially sensitive to these changes.

Building a GraphRAG system gave us a deep, hands-on understanding of AI retrieval, knowledge graphs, and LLM interaction. While the process was more difficult and time-consuming than expected, it also taught us the importance of system design, prompt clarity, and modular architecture.

---

### 5.2 Using GraphRAG Accelerator

The **GraphRAG Accelerator** is a ready-to-deploy solution that extends the `graphrag` Python library into a production-grade API hosted on Azure. Designed to scale with demand, this accelerator enables high-performance indexing and querying of knowledge graphs for enterprise use.

#### Overview

This accelerator simplifies the process of deploying a fully managed GraphRAG service on Azure, providing API endpoints to:

- Trigger **indexing pipelines**.
- Query the **knowledge graph** for context-enriched responses.

It leverages Azure services such as Azure OpenAI, Azure Kubernetes Service (AKS), Azure Container Registry, and Azure API Management. While powerful, it’s important to note that this setup can incur **significant costs**, especially when auto-scaling or large-scale indexing are involved.

#### Benefits of the GraphRAG Accelerator

- **Hosted API Service**: Easily trigger GraphRAG operations (indexing, querying) via RESTful endpoints.
- **Enterprise-Ready**: Auto-scaling, RBAC support, and integration with Azure OpenAI make it ideal for production use cases.
- **Dev Container Support**: A DevContainer setup ensures that required tools are pre-installed for easier local development and deployment.

#### Practical Insights from Deployment

In our project, we tested this accelerator extensively. While the setup is streamlined through scripts and Bicep files, **we encountered limitations** due to using an Azure student account. Key Azure services required for deployment (e.g., Azure OpenAI or APIM) were restricted, preventing us from completing the setup with default configurations.

To overcome this, we had to **upgrade our Azure subscription by attaching a personal credit card**, which allowed access to the required services and quotas (e.g., GPT-4 Turbo, embeddings).

#### How to Deploy the Accelerator

1. **Install prerequisites**: Tools like Azure CLI, Docker, Helm, kubectl, jq, yq, and others are needed. Opening the project in a VS Code DevContainer installs them automatically.
2. **Register Azure providers**: Required providers include `Microsoft.OperationsManagement`, `Microsoft.Compute`, and `Microsoft.AlertsManagement`.
3. **Prepare Azure**: Login, set your subscription, and create a resource group.
4. **Configure deployment**: Edit `infra/deploy.parameters.json` with model names, API endpoints, quotas, and resource names.
5. **Deploy**: Run `bash deploy.sh -p deploy.parameters.json`. The first deployment may take 40–50 minutes.
6. **Access and test**: Once deployed, use the Quickstart notebook or navigate to `<APIM_gateway_url>/manpage/docs` to interact with the APIs.

#### Conclusion

Using the **GraphRAG Accelerator** offers a powerful way to deploy a scalable, API-based GraphRAG system in the cloud. It is particularly suited for enterprise environments where robust infrastructure, user management, and scalability are essential.

However, our experience showed that despite the clear benefits, the setup is **not plug-and-play**, especially when using limited Azure accounts such as student subscriptions. Access restrictions and quota limitations can become major blockers, and resolving them may require a paid upgrade.

Overall, the Accelerator is a great choice **if you have the technical expertise, proper permissions, and budget**. It delivers strong performance, flexibility, and a robust framework to test and productionize GraphRAG workflows. For smaller-scale or experimental projects, lighter setups (e.g., local implementations with `graphrag`) might be a better starting point.

---

### 5.3 Using GraphRAG with AWS

Amazon Web Services (AWS) provides a robust and production-grade environment to implement GraphRAG solutions by combining powerful services such as **Amazon Neptune** (graph database), **Amazon Bedrock** (foundational models like Claude and Titan), and **Amazon SageMaker** (for orchestration and experimentation via Jupyter notebooks).

In our project, we explored how to deploy GraphRAG using AWS components to reason over structured data with LLMs. We worked with two complementary approaches:

- A **custom LlamaIndex-based GraphRAG pipeline** running on Neptune + Bedrock  
- The official **GraphRAG Toolkit**, recently open-sourced by AWS, enabling developers to rapidly prototype graph-augmented RAG systems.



#### Architecture Overview

A typical GraphRAG workflow on AWS follows these high-level steps:

1. **Data Ingestion and Graph Indexing**  
   Documents (e.g., web pages, PDFs, JSON) are parsed and chunked. Then, entities, facts, and relationships are extracted to populate a knowledge graph in **Amazon Neptune**. These elements are enriched with vector embeddings (stored in OpenSearch or other vector DBs).

2. **Retrieval Step**  
   When a user query is submitted (via notebook or API), relevant subgraphs are retrieved from Neptune using Cypher queries. Optional NL2Cypher modules allow translating natural language questions into graph queries.

3. **Reasoning with LLMs**  
   The extracted data is passed to a **foundation model** (e.g., Claude 3 Sonnet via Bedrock). The LLM generates an answer based on both the original prompt and the contextual information retrieved from the graph.

4. **Response Generation**  
   The system produces accurate, grounded, and context-aware answers, often outperforming classical RAG which relies solely on vector similarity.

---

#### Our Implementation

We deployed a simplified GraphRAG system based on AWS documentation:

- **Graph database**: Amazon Neptune (serverless)  
- **LLM orchestration**: Amazon Bedrock via LlamaIndex  
- **Interface**: Jupyter notebooks hosted on SageMaker  
- **Toolkit**: [graphrag-toolkit](https://github.com/awslabs/graphrag-toolkit)


#### Benefits of Using AWS for GraphRAG

- **Scalable infrastructure**: Neptune and Bedrock support production-ready workloads with managed scaling.  
- **Seamless integration**: Bedrock integrates natively with several LLMs (Anthropic, Cohere, Amazon Titan, etc.), reducing configuration complexity.  
- **Rapid prototyping**: With the open-source GraphRAG Toolkit, developers can build indexing pipelines and search workflows using Python and LlamaIndex.  
- **Hybrid retrieval strategies**: AWS supports both semantic search (via vector stores) and structured graph traversal for better relevance.



#### Limitations Encountered

Due to **student account restrictions**, we faced deployment limitations, especially with services requiring elevated permissions or quotas (e.g., Bedrock models, SageMaker notebooks). As a workaround, we had to connect a **personal credit card** to access these features and complete the tests.

Additionally, running LLMs like Claude or Titan at scale through Bedrock can incur significant costs during development if not properly optimized.


#### Conclusion

Using AWS for GraphRAG allowed us to explore production-grade implementations of knowledge-augmented generation. The combination of Neptune, Bedrock, and LlamaIndex made it possible to reason over complex graphs and generate user-specific, explainable outputs.

While initial setup requires time and permissions, AWS provides all the components needed to go from prototype to scalable application — whether via the GraphRAG Toolkit or custom-built stacks.


### 5.4 Using GraphRAG with Puppy Graph


Although we did **not test PuppyGraph** in our implementation, we included it in our research as a compelling and innovative alternative worth exploring.

**PuppyGraph** is a next-generation graph analytics engine designed to instantly transform existing relational databases into graph models—without any ETL. This is a radically different approach compared to traditional graph databases, with a focus on simplicity, performance, and direct integration into existing systems.

With PuppyGraph, it is theoretically possible to build a GraphRAG application in just minutes, leveraging a scalable engine, native support for **Gremlin** and **Cypher**, and seamless compatibility with tools like **LangChain** and **OpenAI**.

---

### General Overview (Based on Documentation)

#### Zero ETL Approach
Unlike traditional setups requiring data to be extracted, transformed, and loaded into a dedicated graph database, PuppyGraph connects directly to existing data lakes and warehouses.  
Tables in **PostgreSQL** or **MySQL** can be instantly treated as graph nodes and edges—no duplication required.

#### Petabyte-Scale Performance
PuppyGraph claims to execute complex queries (e.g., 10-hop traversals) in just seconds—even on petabyte-scale datasets.  
This is achieved through a clear separation of compute and storage, and by leveraging distributed query execution.

#### Simplified Management & Security
No extra user or permission management is needed. PuppyGraph reuses permissions from your existing database, reducing complexity and keeping data securely within your environment.

#### Native Gremlin & Cypher Support
PuppyGraph supports both **Gremlin** (imperative style) and **Cypher** (declarative style), offering flexibility for developers to query graphs using their preferred language.

#### Intelligent GraphRAG Agent
The integrated **PuppyGraphAgent** can plan multi-step graph queries, reason through graph structure, and dynamically adapt its approach.  
Built on **LangChain** and **OpenAI GPT-4o**, the agent follows a **Chain-of-Thought** methodology to explain its reasoning process at every step.

---

### Conclusion

While we did not integrate or test PuppyGraph in our project, it appears to offer a **modern and practical vision of GraphRAG** — one that reduces setup friction and accelerates deployment.

Its **Zero ETL** approach and support for existing SQL databases could make it an attractive solution for teams seeking rapid experimentation without heavy infrastructure.

For future iterations or teams working with relational data, **PuppyGraph could be a powerful candidate to explore further.**

## 6. Comparative Evaluation of GraphRAG Approaches

This section presents a detailed comparison of three GraphRAG-based architectures using a fixed dataset and a consistent set of customer support questions across six thematic categories:

* **Returns & Refunds**
* **Shipping**
* **Orders**
* **Account**
* **Contact Channels**
* **Complex or Linked Questions**

The compared solutions are:

1. **Azure Cognitive Search + OpenAI (Cloud)**
2. **Custom GraphRAG Bot (Neo4j + OpenAI API)**
3. **Local GraphRAG via Docker** *(Evaluation in progress)*

---

## Detailed Evaluation — Azure Accelerator

### Returns & Refunds

| Question                            | Response                                           | Quality   | Completeness | Detail                              | Time |
| ----------------------------------- | -------------------------------------------------- | --------- | ------------ | ----------------------------------- | ---- |
| How do I return a physical product? | ✅ Structured, with 3 sections and link to refund. | Excellent | Complete     | Explains policy, steps, and contact | 17s  |
| What’s your return policy?         | ✅ Structured, clear logic.                        | Excellent | Complete     | Business-oriented explanation       | 22s  |
| Refund for digital product?         | ❌ "Unable to answer"                              | Poor      | None         | No alternative or fallback          | 8s   |
| How long do refunds take?           | ✅ Clear customer and business impact              | Excellent | Complete     | Strategic and well-worded           | 12s  |

### Shipping

| Question                     | Response              | Quality | Completeness | Detail | Time |
| ---------------------------- | --------------------- | ------- | ------------ | ------ | ---- |
| Do you ship to Canada?       | ❌ "Unable to answer" | Poor    | None         | N/A    | 11s  |
| Countries in shipping zones? | ❌                    | Poor    | None         | N/A    | 39s  |
| Customs fees included?       | ❌                    | Poor    | None         | N/A    | 30s  |

### Orders

| Question                     | Response                       | Quality   | Completeness | Detail                                   | Time |
| ---------------------------- | ------------------------------ | --------- | ------------ | ---------------------------------------- | ---- |
| Track my order               | ✅ Mentions entities and tools | Good      | Complete     | Precise and structured                   | 42s  |
| I haven’t received my order | ✅ Step-by-step                | Excellent | Complete     | Live chat, tracking, shipping zone check | 31s  |
| Cancel an order?             | ❌ No data                     | Poor      | None         | No attempt to rephrase                   | 5s   |

### Account

| Question           | Response               | Quality | Completeness | Detail                             | Time |
| ------------------ | ---------------------- | ------- | ------------ | ---------------------------------- | ---- |
| Reset password     | ✅ Uses ACCOUNT entity | Good    | Complete     | Contextualized with security notes | 26s  |
| Forgot credentials | ❌ No data             | Poor    | None         | None provided                      | 4s   |

### Contact Channels

| Question  | Response                     | Quality   | Completeness | Detail                         | Time |
| --------- | ---------------------------- | --------- | ------------ | ------------------------------ | ---- |
| Email     | ✅ Clear and contextual      | Very good | Complete     | Uses email as official channel | 37s  |
| Live chat | ✅ Available, explains usage | Very good | Complete     | Real-time resolution emphasis  | 8s   |

### Complex / Linked Questions

| Question                                | Response                             | Quality   | Completeness | Detail                                   | Time |
| --------------------------------------- | ------------------------------------ | --------- | ------------ | ---------------------------------------- | ---- |
| Returns & refunds for physical products | ✅ Explains linked logic             | Excellent | Complete     | Connects policy, timeline, communication | 26s  |
| Refund delay after return               | ⚠️ Timeline mentioned, no duration | Moderate  | Partial      | Misses exact duration                    | 17s  |
| Best way to contact support             | ✅ Email justified                   | Very good | Complete     | Logically justified                      | 28s  |

### Summary: Azure

| Criteria              | Azure Cognitive Search + OpenAI |
| --------------------- | ------------------------------- |
| Global Accuracy       | ⭐⭐⭐⭐☆                      |
| Answer Completeness   | ⭐⭐⭐☆                        |
| Reasoning (Multi-hop) | ⚠️ Moderate                   |
| Response Time         | ⏳ 8–42s                       |
| Answer Structure      | ✅ Excellent                    |
| Failure Rate          | 🔴 5/16 (~31%)                  |

---

## Detailed Evaluation — GraphRAG Bot 

### Returns & Refunds

| Question                            | Response                      | Quality   | Completeness | Detail                          | Time          |
| ----------------------------------- | ----------------------------- | --------- | ------------ | ------------------------------- | ------------- |
| How do I return a physical product? | ✅ Website/email/chat options | Good      | Partial      | Lacks process detail            | 10s (2nd try) |
| What’s your return policy?         | ✅ General definition         | Moderate  | Partial      | Refers policy without specifics | 11s           |
| Refund for digital product?         | ✅ Possible                   | Good      | Partial      | No terms or limits given        | 11s           |
| How long do refunds take?           | ✅ 3-5 business days          | Excellent | Complete     | Straightforward answer          | 9s            |

### Shipping

| Question                     | Response | Quality | Completeness | Detail               | Time |
| ---------------------------- | -------- | ------- | ------------ | -------------------- | ---- |
| Do you ship to Canada?       | ✅ Yes   | Good    | Complete     | Short but correct    | 8s   |
| Countries in shipping zones? | ❌       | Poor    | None         | No effort to explain | 9s   |
| Customs fees included?       | ❌       | Poor    | None         | No fallback offered  | 9s   |

### Orders

| Question                     | Response                 | Quality  | Completeness | Detail                       | Time |
| ---------------------------- | ------------------------ | -------- | ------------ | ---------------------------- | ---- |
| Track my order               | ✅ Website instructions  | Good     | Complete     | Simple, usable               | 10s  |
| I haven’t received my order | ✅ Requests order number | Moderate | Partial      | Helpful tone, no action list | 12s  |
| Cancel an order?             | ✅ Possible              | Moderate | Partial      | No conditions explained      | 8s   |

### Account

| Question           | Response                       | Quality   | Completeness | Detail           | Time |
| ------------------ | ------------------------------ | --------- | ------------ | ---------------- | ---- |
| Reset password     | ✅ Reset instructions provided | Excellent | Complete     | Clear and direct | 11s  |
| Forgot credentials | ✅ Reset guidance + help       | Excellent | Complete     | Offers help      | 12s  |

### Contact Channels

| Question  | Response          | Quality | Completeness | Detail                        | Time |
| --------- | ----------------- | ------- | ------------ | ----------------------------- | ---- |
| Email     | ✅ Email provided | Good    | Complete     | Suggests email as main option | 11s  |
| Live chat | ✅ Available      | Good    | Complete     | Lists areas it covers         | 11s  |

### Complex / Linked Questions

| Question                                | Response              | Quality   | Completeness | Detail                | Time |
| --------------------------------------- | --------------------- | --------- | ------------ | --------------------- | ---- |
| Returns & refunds for physical products | ✅ Summarized clearly | Very good | Complete     | Solid linking         | 10s  |
| Refund delay after return               | ✅ 3–5 days          | Excellent | Complete     | Accurate timeframe    | 11s  |
| Best way to contact support             | ✅ Email/chat/website | Good      | Complete     | No best method argued | 12s  |

### Summary: Neo4j Bot

| Criteria              | GraphRAG Bot (Neo4j + OpenAI) |
| --------------------- | ----------------------------- |
| Global Accuracy       | ⭐⭐⭐⭐☆                    |
| Answer Completeness   | ⭐⭐⭐☆                      |
| Reasoning (Multi-hop) | ✅ Very good                  |
| Response Time         | ⚡ 8–12s                     |
| Answer Style          | ✅ Conversational             |
| Failure Rate          | ⚠️ 2/16 (~12%)              |

---

## Local GraphRAG (Docker)

Currently under evaluation. Initial response times (seconds):

| Question                | Time (s) |
| ----------------------- | -------- |
| Return physical product | 195      |
| Ship to Canada          | 233      |
| Track order             | 384      |
| Reset password          | 492      |
| Contact by email        | 83       |
| Complex return/refund   | 186      |

Final quality and coverage analysis pending full results.

---

## Comparative Summary Table

| Criteria / Feature  | Azure Cognitive Search + OpenAI | GraphRAG Bot (Neo4j + OpenAI) | Local GraphRAG (Docker)   |
| ------------------- | ------------------------------- | ----------------------------- | ------------------------- |
| Setup Complexity    | ⭐⭐☆☆☆                      | ⭐⭐⭐☆                      | ⭐⭐⭐⭐☆ (technical)    |
| Cost Predictability | ❌ Cloud-based                  | ⚠️ API cost varies          | ✅ Free (local inference) |
| Answer Precision    | ⭐⭐⭐⭐☆                      | ⭐⭐⭐⭐☆                    | 🔄 To be tested           |
| Reasoning Quality   | ⚠️ Moderate                   | ✅ Excellent                  | ✅ (Expected)             |
| Response Time       | ⏳ 8–42s                       | ⚡ 8–12s                     | 🐢 80–490s               |
| Structure / Clarity | ✅ Very good                    | ✅ Conversational             | 🔄 Pending                |
| Failure Rate        | 🔴 ~31%                         | ⚠️ ~12%                     | 🔄 Unknown                |
| Offline Capability  | ❌                              | ❌                            | ✅                        |

## 8. Conclusion

Our exploration of GraphRAG has revealed its transformative potential in enhancing Retrieval-Augmented Generation with structured, semantic understanding.

We tested and compared **three main approaches**:

- **GraphRAG with Azure**: Using Cognitive Search and OpenAI, we deployed a cloud-based system with API endpoints. It offered good structure and reasoning but faced restrictions due to our student account and incurred potential costs for extended usage.

- **GraphRAG with AWS**: Built with Amazon Neptune, Bedrock, and LlamaIndex, our implementation allowed graph-based reasoning over structured data. Although powerful, the setup required elevated permissions, leading us to use a personal credit card to access Bedrock and SageMaker features.

- **Custom GraphRAG Application**: We developed our own stack from scratch using LangChain, OpenAI, and graph databases like Neo4j. This gave us complete control over schema design, retrieval strategies, prompt engineering, and UI logic. While more complex to implement and maintain, this approach proved the most flexible and educational.

We also analyzed **PuppyGraph** as an **alternative we did not test directly**. Based on its documentation, it presents an interesting “Zero ETL” solution designed to simplify the entire GraphRAG pipeline by removing infrastructure overhead. It could be a valuable option for future projects using existing SQL data and requiring minimal deployment time.

---

Our conclusion is that **GraphRAG is a powerful but non-trivial enhancement to classical RAG**. Its success depends on several factors:

- The structure and quality of the knowledge base  
- The type of queries and reasoning required  
- The chosen infrastructure (local, cloud, or hybrid)  
- The team’s experience with graph technologies and LLM orchestration

In our case, we found that **cloud-based services (AWS, Azure)** offered fast results and managed services but introduced permission and cost constraints. In contrast, **custom implementation** required more development effort but offered the best control and understanding.

For future improvements, we plan to:

- Refine our prompt engineering techniques  
- Explore lightweight deployments with open-source LLMs  
- Possibly evaluate PuppyGraph in a real scenario  

GraphRAG is still a young but promising field — and it's clearly shaping the future of AI systems that reason, adapt, and retrieve information with higher precision and explainability.

---

## 9. References

Bouchard, L. (2024, 12. August). When to Use GraphRAG. **https://www.linkedin.com/pulse/when-use-graphrag-louis-fran%C3%A7ois-bouchard-evkoe**

Bryan, J. (n.d.). How Precina Health Uses Memgraph and GraphRAG to Revolutionize Type 2 Diabetes Care with Real-Time Insights. Memgraph. **https://memgraph.com/blog/precina-health-memgraph-graphrag-type-2-diabetes-care**

Définition du PageRank - agence SEO.fr . (2024, 5 mars). Agence SEO.fr. **https://www.seo.fr/definition/pagerank#:~:text=Le%20PageRank%20est%20un%20algorithme,le%20co%2Dfondateur%20de%20Google.**

Evolution of AI in information retrieval | Restackio . (s. d.). **https://www.restack.io/p/information-retrieval-answer-evolution-of-ai-cat-ai**

Fokou, K. (2019, 11 juin).  *NLP & modèles de langage | Smals Research* . **https://www.smalsresearch.be/nlp-modeles-de-langue/**

Hafeez, M. (2024, 1. September). GraphRAG: The Unique Value that Oracle Database 23ai Brings to the Table. **https://www.linkedin.com/pulse/graphrag-unique-value-oracle-database-23ai-brings-table-hafeez-9bj1f**

Azure-Samples. (s. d.). GitHub - Azure-Samples/graphrag-accelerator : One-click deploy of a Knowledge Graph powered RAG (GraphRAG) in Azure. GitHub. **https://github.com/Azure-Samples/graphrag-accelerator?tab=readme-ov-file**

Harsh, K., & Harsh, K. (2024, 19 novembre). *What is Retrieval-Augmented Generation (RAG) ? * Bright Data. **https://brightdata.com/blog/web-data/rag-explained#:~:text=One%20major%20issue%20is%20the,back%20irrelevant%20or%20inaccurate%20documents.**

Korland, G. (2025, 6. Februar). What is GraphRAG? Types, Limitations & When to Use. FalkorDB Knowledge Graph Database. **https://www.falkordb.com/blogs/what-is-graphrag/**

PuppyGraph Docs. (n.d.). **https://docs.puppygraph.com/**

Introducing the GraphRAG Toolkit. (2025, 27 January). Amazon Web Services, Inc. **https://aws.amazon.com/fr/blogs/database/introducing-the-graphrag-toolkit/**

Martineau, K. (2024, 13. November). What is retrieval-augmented generation? IBM Research. **https://research.ibm.com/blog/retrieval-augmented-generation-RAG**

Merritt, R. (2025, 31 janvier).  *What Is Retrieval-Augmented Generation aka RAG | NVIDIA Blogs* . NVIDIA Blog. **https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/?utm_source=chatgpt.com**

Using knowledge graphs to build GraphRAG applications with Amazon Bedrock and Amazon Neptune. (2024, 1 August). Amazon Web Services, Inc. **https://aws.amazon.com/fr/blogs/database/using-knowledge-graphs-to-build-graphrag-applications-with-amazon-bedrock-and-amazon-neptune/**

SivaParam. (2024, 25. September). Unlocking Insights: GraphRAG & Standard RAG in Financial Services. **https://techcommunity.microsoft.com/blog/azure-ai-services-blog/unlocking-insights-graphrag--standard-rag-in-financial-services/4253311**

Sparkbit. (2025, 9. Januar). GraphRAG - where and how is it used. **https://www.linkedin.com/pulse/graphrag-where-how-used-sparkbit-eawaf**

What is RAG? - Retrieval-Augmented Generation AI Explained - AWS. (n.d.). Amazon Web Services, Inc. **https://aws.amazon.com/what-is/retrieval-augmented-generation/?nc1=h_ls**

Welcome - GraphRAG. (n.d.). **https://microsoft.github.io/graphrag/**

---
