# This class is a base exception class for all the other exceptions in this module.
class PerceptorAPIException(Exception):
    pass

# This exception is raised when a file that is being uploaded to the system is empty.
class FileIsEmptyException(PerceptorAPIException):
    pass

# This exception is raised when a file that is being uploaded to the system has a MIME type that is not supported by the system.
class FileIsNotSupported(PerceptorAPIException):
    pass

# This exception is raised when a file that is being uploaded to the system exceeds the maximum file size limit.
class FileIsTooLarge(PerceptorAPIException):
    pass

# This exception is raised when a request to the system is not valid or malformed.
class RequestIsNotValid(PerceptorAPIException):
    pass

# This exception is raised when a request to the system times out and does not receive a response within a specified amount of time.
class TimeoutError(PerceptorAPIException):
    pass
