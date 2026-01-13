from service_container import llm_service

def get_llm_model():
    if llm_service is None:
        raise RuntimeError("LLM not initailized")
    return llm_service
    


