import structlog
import logging

class Cloud_Custom_Logger():
    _configured=False
    @classmethod
    def get_cloud_custom_logger(cls,name:str):
        if not cls._configured:
            handlers=[logging.StreamHandler()]
            logging.basicConfig(
                level=logging.INFO,
                handlers=handlers
            )
            structlog.configure(
                processors=[
                    structlog.processors.TimeStamper(fmt="iso",utc=True),
                    structlog.processors.add_log_level,
                    structlog.processors.CallsiteParameterAdder(
                        {
                            structlog.processors.CallsiteParameter.FILENAME,
                            structlog.processors.CallsiteParameter.LINENO
                        }
                    ),
                    structlog.processors.JSONRenderer()
                ],
                logger_factory=structlog.stdlib.LoggerFactory(),
                cache_logger_on_first_use=True
            )  
            cls._configured=True
        return structlog.get_logger(name)  

