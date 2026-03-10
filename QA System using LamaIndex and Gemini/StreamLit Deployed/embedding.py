from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.core import Settings

def download_gemini_embedding(model,document):
    embedding = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    Settings.llm = model
    Settings.embed_model = embedding
    Settings.chunk_size = 512
    Settings.chunk_overlap = 40
    
    index = VectorStoreIndex.from_documents(document)
    index.storage_context.persist(persist_dir="./storage")
    query_engine = index.as_query_engine()
    
    return query_engine