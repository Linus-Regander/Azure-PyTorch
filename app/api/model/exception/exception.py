class AppException(Exception):
    """
    Custom class for application exceptions.
    """
    
    def __init__(self, message: str, error_code: int = 500):
        super().__init__(message)
        self.message = message
        self.error_code = error_code