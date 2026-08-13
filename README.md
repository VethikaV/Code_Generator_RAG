AI Code Generator

An AI-powered code generation assistant built with Streamlit, LangChain, LLaMA 3, Groq, Hugging Face MiniLM, ChromaDB, and LangSmith.

The application converts natural-language programming problems into code and can optionally use Retrieval-Augmented Generation (RAG) to ground the generated code in user-provided reference documents.

Overview

Traditional code-generation systems depend mainly on the knowledge encoded in an LLM. This project adds a retrieval layer so that users can provide domain-specific material such as documentation, notes, or reference files.

The system supports two modes:

Code Generator — generates code directly from the user's programming problem.

RAG Code Generator — retrieves relevant information from uploaded documents and uses that context while generating the code.

The interface is implemented using Streamlit, the LLM is accessed through ChatGroq, document embeddings are generated using Hugging Face MiniLM, and the embeddings are stored and retrieved using ChromaDB. LangSmith provides tracing and observability for the LangChain pipeline.

Key Features

Natural-language to code generation

Multiple programming languages:

Python

JavaScript

C++

Java

Ruby

Go

PHP

Optional RAG mode for context-aware code generation

Upload reference files for RAG processing

Semantic document retrieval using embeddings

Local ChromaDB vector store

LLaMA 3 based code generation through Groq

LangChain prompt and retrieval orchestration

LangSmith tracing, debugging, and observability

Syntax-highlighted code output in the Streamlit interface

Architecture

The following architecture represents the main application and RAG pipeline:

flowchart TD
    U[User] --> UI[Streamlit UI<br/>app.py]

    UI --> Q{RAG Enabled?}

    Q -->|No| C[chain.py<br/>Code Generation Chain]
    Q -->|Yes| R[chain.py<br/>RAG Generation Chain]

    UI --> FI[RAG File Ingestion]
    FI --> UT[utils.py<br/>Document Processing]
    UT --> CH[Text Splitting]
    CH --> EMB[Hugging Face MiniLM<br/>Embeddings]
    EMB --> DB[(ChromaDB<br/>Vector Store)]

    R --> RET[Similarity Retrieval<br/>vectordb.py]
    RET --> DB
    RET --> CTX[Relevant Context]
    CTX --> P[Prompt Template<br/>prompt.py]

    C --> P
    P --> LLM[ChatGroq<br/>LLaMA 3]
    LLM --> OUT[Generated Code]
    OUT --> UI

    LS[LangSmith<br/>Tracing & Monitoring] -. monitors .-> C
    LS -. monitors .-> R
    LS -. monitors .-> LLM

RAG Flow

flowchart TD
    DOC[Reference Document] --> PROC[Document Processing]
    PROC --> CHUNK[Text Chunking]
    CHUNK --> EMB[MiniLM Embeddings]
    EMB --> DB[(ChromaDB)]

    Q[User Problem] --> RET[Semantic Similarity Search]
    DB --> RET
    RET --> CTX[Relevant Context]

    CTX --> PROMPT[RAG Prompt]
    Q --> PROMPT
    PROMPT --> LLM[LLaMA 3 via Groq]
    LLM --> OUT[Generated Code]

How It Works

1. User Input

The user selects a programming language and describes the coding problem in natural language.

Example:

Language: Python
Problem: Write a function to add two numbers

2. Without RAG

When RAG is disabled:

User Problem
    ↓
Prompt Template
    ↓
LLaMA 3 via ChatGroq
    ↓
Generated Code

3. With RAG

When RAG is enabled:

User Problem
    ↓
Embedding / Similarity Search
    ↓
ChromaDB
    ↓
Relevant Documents
    ↓
RAG Prompt + User Problem
    ↓
LLaMA 3 via ChatGroq
    ↓
Context-Aware Code

4. Document Ingestion

Users can upload reference material through the RAG File Ingestion section. The application processes the uploaded material, splits it into chunks, creates embeddings, and stores them in ChromaDB.

The project report describes the document-processing pipeline using a recursive text splitter with a chunk size of 1000 and an overlap of 200.

5. Monitoring

LangSmith is integrated as the observability layer. It can be used to inspect:

User inputs

Prompt execution

Retrieval steps

LLM calls

Outputs

Latency

Token usage

Errors and debugging information

Tech Stack

Component

Technology

Frontend / UI

Streamlit

Programming Language

Python

LLM

LLaMA 3

LLM API

Groq / ChatGroq

LLM Framework

LangChain

Embedding Model

Hugging Face all-MiniLM-L6-v2

Vector Database

ChromaDB

Observability

LangSmith

Document Processing

PyMuPDF / PyPDFLoader, python-docx, pandas

Environment Management

python-dotenv

Project Structure

AI-Code-Generator/
│
├── Assets/
│   ├── 01-code-generator-ui.png
│   ├── 02-rag-file-ingestion.png
│   ├── 03-python-code-output.png
│   ├── 04-java-code-output.png
│   └── 05-langsmith-trace.png
│
├── chroma_db/
│   └── Local ChromaDB persistence
│
├── app.py
│   └── Streamlit application and UI
│
├── chain.py
│   └── Standard and RAG generation chains
│
├── model.py
│   └── ChatGroq and Hugging Face model configuration
│
├── prompt.py
│   └── Code-generation and RAG prompt templates
│
├── utils.py
│   └── Document processing and text splitting
│
├── vectordb.py
│   └── ChromaDB initialization, indexing and retrieval
│
├── requirement.txt
│   └── Python dependencies
│
└── .gitignore

__pycache__ files and local vector-store data are generally environment-specific. Keep secrets such as API keys out of Git.

Installation

1. Clone the repository

git clone <YOUR-GITHUB-REPOSITORY-URL>
cd <YOUR-REPOSITORY-FOLDER>

2. Create a virtual environment

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

3. Install dependencies

pip install -r requirement.txt

4. Configure API credentials

Create a .env file in the project root and add the API credentials required by your ChatGroq/LangSmith configuration.

Example:

GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=code_generator

Do not commit .env or API keys to GitHub.

5. Run the application

streamlit run app.py

The Streamlit application will open in your browser.

Usage

Generate Code

Open the Code Generator RAG section.

Select the programming language.

Enter the coding problem.

Enable or disable RAG.

Click Generate Code.

Review and copy the generated code.

Use RAG

Open RAG File Ingestion.

Upload a reference document.

Allow the application to process and store the document in ChromaDB.

Return to Code Generator RAG.

Enable RAG for better suggestions.

Enter a coding problem related to the uploaded material.

Generate the context-aware code.

Sample Screenshots

Code Generator Interface



RAG File Ingestion



Python Code Generation



Java Code Generation



LangSmith Monitoring



Example

Input

Programming Language: Python

Problem:
Write a code to add two numbers

Generated Output

def add_numbers(a, b):
    return a + b

The application displays the generated result directly in the Streamlit interface.

RAG vs. Non-RAG

Mode

Context Source

Use Case

Standard

LLM knowledge + user prompt

General programming tasks

RAG

LLM + retrieved user documents

Domain-specific or reference-driven coding

RAG is useful when the generated code needs to reflect information contained in documentation, project notes, or other reference material.

Core Modules

app.py

Handles the Streamlit interface, user inputs, language selection, RAG toggle, file uploads, and code display.

chain.py

Contains the standard generation chain and RAG generation chain.

model.py

Creates the ChatGroq LLM configuration and the Hugging Face embedding model.

prompt.py

Defines the standard and RAG-enabled prompt templates used for code generation.

utils.py

Processes uploaded documents and splits their content into smaller chunks for retrieval.

vectordb.py

Initializes ChromaDB, stores document chunks, and retrieves relevant documents using similarity search.

Why RAG?

A standalone LLM can generate code from its learned knowledge, but it may not have access to project-specific documentation or newly supplied reference material.

RAG adds an external knowledge layer:

LLM
+
External Reference Knowledge
=
More Context-Aware Generation

This makes the system suitable for educational, project-specific, and documentation-driven coding tasks.

Future Enhancements

Support additional document loaders for all UI-supported file types

Add code execution and automated testing

Add syntax and security validation

Add conversation history

Add downloadable generated code files

Add support for additional LLM providers

Improve retrieval with configurable top-k similarity search

Add evaluation metrics for generated code quality

Add deployment using Docker or a cloud platform
