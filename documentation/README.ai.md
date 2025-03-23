#  OpenAI & Ollama - LLMs for Natural Language Movie Q&A

## What is OpenAI / Ollama?

This project began using **OpenAI's GPT-4** API for natural language generation, due to its accuracy and power. However, due to **token-based pricing**, costs quickly added up (as shown in the screenshot), which led to switching to **Ollama**, a local LLM runtime that allows models like **Mistral**, **LLaMA2**, or **Gemma** to run **entirely offline** on your machine — for free.

Ollama is ideal for local development, prototypes, and low-latency applications. It serves as a drop-in replacement for OpenAI’s chat interface with minimal code changes.

---

## Installation

### OpenAI

1. Sign up at [https://platform.openai.com](https://platform.openai.com)
2. Create an API key under your account settings
3. Install the OpenAI Python client:
   ```bash
   pip install openai
   ```
4. Add your key to your environment variables or .env file:
    ```
    OPENAI_API_KEY=your_key_here
    ```

### Ollama (Local LLM)
1. Download from https://ollama.com
2. Install the binary for your OS (macOS, Windows, Linux)
3. Run the installer and verify with:
    ```
    ollama run mistral
    ```
4. Install Python wrapper:
    ```
    pip install ollama
    ```

## How It’s Used in This Project

The **AI model** is used to generate **intelligent, multi-hop** answers about movies, based on retrieved graph data (from Neo4j) and semantic vector matches (from FAISS). Here's how each version was integrated:

**OpenAI**: We used GPT-4 via API to generate context-aware answers. Queries and structured knowledge were sent as messages using the OpenAI Chat API.

**Ollama**: A simple and free replacement. Ollama loads a model like mistral locally and processes messages in a similar JSON format.

---

## Running 

**OpenAI**
Make sure you have a valid key and call the API with:
    ```
    import openai
    openai.api_key = "your-key"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Your prompt"}]
    )
    ```

**With Ollama**
After installing the model, just run:
    ```
    ollama run mistral
    ```
And interact with it via the ollama Python client or CLI.

## Why We Used 

We initially used **OpenAI** for its unmatched accuracy and multi-hop reasoning power. However, token usage **costs escalated quickly** — as it cost us 6 Dollar for only a few days of testing. To reduce dependency on paid APIs and allow offline/local use, we switched to **Ollama**.

This made the system:

- Cost-efficient (free)
- Fully local / privacy-friendly
- Fast — no latency or internet needed

---

## Advantages of OpenAI

- Best-in-class performance
- Deep context understanding & multi-hop reasoning
- Cloud-hosted, no setup required
- Supports multiple models and tools (functions, vision, etc.)

## Advantages of Ollama
 
- Free and local — no token costs
- Simple setup
- Runs on your machine (privacy-by-design)
- Works well with smaller LLMs like Mistral or LLaMA2


---

## Disadvantages of OpenAI

- Expensive at scale (per-token pricing)
- Requires internet connection
- May leak sensitive data if not handled securely

## Disadvantages of Ollama

- Less accurate than OpenAI
- Requires system resources (RAM/CPU)
- Model quality depends on what you install (e.g., Mistral vs GPT-4)

---

## Alternatives to OpenAI / Ollama

| Tool / API             | Type         | Notes                                                    |
|------------------------|--------------|----------------------------------------------------------|
| **Hugging Face Inference** | Cloud API     | Free-tier models, similar interface to OpenAI             |
| **LM Studio**          | Local GUI     | Run local LLMs in a no-code environment                   |
| **GPT4All**            | Local Runtime | Desktop app to run various LLMs offline                  |
| **Google Gemini API**  | Cloud API     | GPT-4 competitor with multimodal capabilities             |
| **Anthropic Claude**   | Cloud API     | Focuses on safe and ethical AI; strong summarization      |

---

## 📝 Summary

We began the project with **OpenAI** because of its powerful capabilities and accurate multi-hop reasoning. However, due to rising API costs, we later switched to **Ollama**, which allows us to run LLMs like Mistral entirely **offline** and **for free**.

This transition helped us keep development local, reduce budget impact, and test more freely. 

For further ideas, we could implement a hybrid approach — run **Ollama** for local development and **OpenAI** for production when high accuracy is needed.

---

## References for this readme file:
- https://platform.openai.com/api-keys
- https://ollama.com/
- https://huggingface.co/
- https://lmstudio.ai/
- https://www.nomic.ai/gpt4all
- https://ai.google.dev/
- https://www.anthropic.com/claude