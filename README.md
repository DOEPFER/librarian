# Librarian 📚

Librarian is an intelligent system developed to automatically organize digital PDF libraries (books). It analyzes the file content and distributes them into "shelves" (folders) based on AI-identified categories and semantic similarity.

## 🚀 How It Works

The workflow is divided into several main stages, optimized for low cost and high precision:

1. **Smart Sampling:** The system extracts only the first 7 pages of the PDF. This ensures enough context (prefaces, tables of contents, and introductions) while saving processing tokens.
2. **Summarizer Agent (LLM):** In this stage, a first Agent analyzes the sample to:
    * **Naming:** Generates a standardized file name based on title, edition, and author.
    * **Summary:** Generates a concise summary of the content.
    * **Tagging:** Creates strategic tags to facilitate future retrieval via RAG (Retrieval-Augmented Generation).
    * *Note: For security reasons, the agent does not have direct write permissions (MCP/Tools) to the file system.*
3. **Semantic Similarity & Embedding:** The system calculates an embedding for the document and compares it against existing files. If a similarity threshold (e.g., >= 0.75) is met, the file is automatically assigned to the same shelf as the most similar existing file.
4. **Librarian Agent (LLM):** If no suitable match is found, a second Agent defines the ideal "shelf" (destination folder hierarchy, up to 3 levels deep) based on the summary and tags.
5. **Organization & Indexing:** The file is renamed and physically moved to the defined category. Finally, the library index and embeddings are updated.

## 🛠️ Tech Stack

* **Language:** Python
* **Agent Framework:** Agno

## 🚧 Project Status

This project is currently **Work in Progress (WIP)**.
Upcoming implementations include improvements in metadata extraction and refinement of classification prompts.