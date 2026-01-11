class AppException(Exception):
    def __init__(
            self,
            message:str,
            *,
            error_code:str,
            status_code:int=500,
            details:dict|None=None,
    ):
        super.__init__(message),
        self.message=message,
        self.error_code=error_code,
        self.status_code=status_code,
        self.details=details or {}

class LLMError(AppException):
    pass


