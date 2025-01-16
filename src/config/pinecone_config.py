import os

from dotenv import load_dotenv
from pinecone import ServerlessSpec
from pinecone.grpc import PineconeGRPC as Pinecone

# Load environment variables from .env file
load_dotenv()

# Initialize Pinecone with your API key
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_environment = os.getenv("PINECONE_ENVIRONMENT")

pc = Pinecone(api_key=pinecone_api_key)

# Set your index name
index_name = "hive-docs-buddy-3"

# Check if the index already exists; if not, create it
if index_name not in [i.name for i in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ),
        deletion_protection="disabled"
    )

# Access the index
pinecone_index = pc.Index(index_name)
