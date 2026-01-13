from fastapi import FastAPI,Request,status
import uvicorn
from fastapi.responses import JSONResponse
from multi_doc_chat.exception.custom_exception import AppException
from multi_doc_chat.config.configSettings import get_settings
from multi_doc_chat.service.llm_service import LLMService
from multi_doc_chat.service import service_container

settings=get_settings()
service_container.llm_service=LLMService(settings)
service_container.llm_service.load_llm()

app=FastAPI(
    title=settings.PROJECT_NAME
)
"""will write this code in lambda handler to handler it globally"""
@app.exception_handler(AppException)
async def app_exception_handler(request:Request,exc:AppException):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message":exc.message}
    )
def main():
    print("Hello from llmops-rag!")


if __name__ == "__main__":
    #main()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
