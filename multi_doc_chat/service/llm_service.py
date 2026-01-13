from multi_doc_chat.config.configSettings import Settings
from langchain_openai import ChatOpenAI

class LLMService():
    def __init__(self,settings:Settings):
        self.API_KEY=settings.OPENAI_API_KEY,
        self.MODEL_NAME=settings.MODEL_NAME,
        self.TEMPERATURE=settings.TEMPERATURE
    """
    we  will load the model once and invoke as many times we want.
    """
    def load_llm(self):
        """
        Load and configure the model.
        """
        return ChatOpenAI(

        )
    def load_embeddings(self):
        """
        Load and configure the embedding model.
        """
    def generate(self):
        """
        generate the content from llm.
        """
