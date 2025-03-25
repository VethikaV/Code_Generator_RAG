
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

def create_chat_groq_model(
    model="llama3-8b-8192",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
):
    
        
    return ChatGroq(
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        timeout=timeout,
        max_retries=max_retries,
        cache=False
    )

def create_hugging_face_embedding_model(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Creates and returns a configured instance of the HuggingFace embeddings model.

    Args:
        model_name -> str: The model to use (default: "sentence-transformers/all-MiniLM-L6-v2").

    Returns:
        HuggingFaceEmbeddings: Configured HuggingFaceEmbeddings model instance
    """
    return HuggingFaceEmbeddings(model_name=model_name)


def create_code_generation_model(language, problem, model="llama3-8b-8192"):
    """
    Creates and returns a configured instance of the ChatGroq model for code generation.

    Args:
        language -> str: The programming language for code generation.
        problem -> str: The problem or task description for code generation.
        model -> str: The model to use (default: "mixtral-8x7b-32768").

    Returns:
        ChatGroq: Configured ChatGroq model instance for code generation.
    """
    prompt = f"Generate a code in {language} to solve the following problem: {problem}"

    # Return a configured model with code generation context
    return ChatGroq(
        model=model,
        temperature=0.5,  # Adjust temperature for more creativity in code generation
        max_tokens=150,  # Set a reasonable token limit for code generation
        cache=False
    )