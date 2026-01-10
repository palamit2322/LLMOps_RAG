from datetime import datetime
import structlog
import logging

class Cloud_Custom_Logger():
    _configured=False
    def get_cloud_custom_logger(self,name:str):

        if not Cloud_Custom_Logger._configured:
            logging.basicConfig(
                level=logging.INFO,
                handlers=[logging.StreamHandler()]
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
        Cloud_Custom_Logger._configured-True

        return structlog.get_logger(name)  

