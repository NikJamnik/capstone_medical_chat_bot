# Dermatology QA Chatbot with RAG
This repository contains the code for a Telegram chatbot that answers questions about dermatology using a Retrieval-Augmented Generation (RAG) model. It integrates a FastAPI backend with OpenAI’s language models and Pinecone vector database for efficient medical question answering. 
The system is trained on a clinical dermatology textbook to provide expert-level responses to user queries. The chatbot is deployed using [Railway](https://railway.com/), enabling easy cloud-based hosting.

# Knowledge base
We use the open-access [textbook]((https://webicdn.com/sdirmember/14/13336/produk/ClinicalDermatology.pdf)) Clinical Dermatology as the source of information for the RAG pipeline. 
## Data access statement
The data used for this project consists of a publicly available textbook:
> Habif, T. P. *Clinical Dermatology*.  
> PDF available at: [https://webicdn.com/sdirmember/14/13336/produk/ClinicalDermatology.pdf](https://webicdn.com/sdirmember/14/13336/produk/ClinicalDermatology.pdf)

This textbook was used solely for academic and non-commercial purposes as a knowledge base for our chatbot.

We do not redistribute the content directly through this repository.  

Users are expected to download the PDF themselves if they wish to reproduce or extend the project.

If your use case is outside educational or research use, please check the copyright terms of the book.

# Repository structure
- `fastapi_backend.py` - Contains the FastAPI backend logic. It exposes an endpoint that receives questions, runs the RAG pipeline, and returns the answer.
- `bot_runner.py` - Contains the code for the Telegram chatbot. It connects with the FastAPI backend to send and receive user questions and answers.
- `requirements.txt` - Lists all necessary Python packages required to run the notebooks, backend, and bot. Install via `pip install -r requirements.txt`
- `dermatology-rag-model-a.ipynb` - A Jupyter notebook exploring QA performance using OpenAI's gpt-3.5-turbo with a simple chunk-based retriever.
- `LLMV2.ipynb` - Another notebook testing gpt-4 with improved chunking, prompt tuning, and use of cosine similarity for better semantic retrieval.

# Getting started
## Get required API keys
1. Get `OPENAI_API_KEY` in the [console](https://platform.openai.com/account/api-keys) to query OpenAI models
2. Get `PINECONE_API_KEY` as in the [instruction](https://docs.pinecone.io/guides/projects/manage-api-keys) for storing / retrieving vector embeddings
3. Get `TELEGRAM_BOT_TOKEN` as in the [tutorial](https://core.telegram.org/bots/tutorial) to operate the Telegram bot
Set them as environment variables.

## Run the notebooks
1. Clone the repository and install the dependencies
`
git clone https://github.com/your-username/dermatology-chatbot.git
cd dermatology-chatbot
pip install -r requirements.txt
`
2. Add your API keys to environment variables or directly into the notebook (not recommended for shared notebooks)
3. Open either `dermatology-rag-model-a.ipynb` or `LLMV2.ipynb` in Jupyter or VSCode
4. Run the cells sequentially to:
- Load and embed documents
- Initialize the retriever
- Query OpenAI with context 

## Run the bot
1. Make sure your FastAPI backend is running locally or on in cloud
2. Start the Telegram bot by running: `python bot_runner.py`
3. Your bot should now respond to dermatology questions via Telegram!

## Deploy the bot
We use [Railway](https://railway.com/) to deploy the FastAPI backend to the cloud, making it accessible to the Telegram bot 24/7 without running it locally. You can create a Railway project, connect your GitHub repo, and add environment variables in the Railway dashboard.
  
