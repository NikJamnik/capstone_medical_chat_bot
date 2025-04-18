# Dermatology QA Chatbot with RAG
This repository contains the code for a Telegram chatbot that answers questions about dermatology using a Retrieval-Augmented Generation (RAG) model. It integrates a FastAPI backend with OpenAI’s language models and Pinecone vector database for efficient medical question answering. 
The system is trained on a clinical dermatology textbook to provide expert-level responses to user queries. The chatbot is deployed using Railway (https://railway.com/), enabling easy cloud-based hosting.

# Knowledge base
We use the open-access textbook Clinical Dermatology (https://webicdn.com/sdirmember/14/13336/produk/ClinicalDermatology.pdf) as the primary source of information for the RAG pipeline. 
### Note on Academic Use
The book is used here solely for academic and research purposes under the assumption that such use falls within fair use / fair dealing for educational projects. If you're unsure whether you can use this data, please consult your institution’s copyright policy.

# Repository structure
- `fastapi_backend.py` - Contains the FastAPI backend logic. It exposes an endpoint that receives questions, runs the RAG pipeline, and returns the answer.
- `bot_runner.py` - Contains the code for the Telegram chatbot. It connects with the FastAPI backend to send and receive user questions and answers.
- `requirements.txt` - Lists all necessary Python packages required to run the notebooks, backend, and bot. Install via `pip install -r requirements.txt`
- `dermatology-rag-model-a.ipynb` - A Jupyter notebook exploring QA performance using OpenAI's gpt-3.5-turbo with a simple chunk-based retriever.
- `LLMV2.ipynb` - Another notebook testing gpt-4 with improved chunking, prompt tuning, and use of cosine similarity for better semantic retrieval.

# Getting started
1. Get **OPENAI_API_KEY** in the [console](https://platform.openai.com/account/api-keys) to query OpenAI models
2. Get **PINECONE_API_KEY** as in the [instruction](https://docs.pinecone.io/guides/projects/manage-api-keys) for storing / retrieving vector embeddings
3. Get **TELEGRAM_BOT_TOKEN** as in the [tutorial](https://core.telegram.org/bots/tutorial) to operate the Telegram bot
