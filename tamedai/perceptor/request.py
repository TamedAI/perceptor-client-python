from io import BytesIO
import mimetypes
import requests
from hashlib import md5
from tamedai.perceptor.exceptions import *
import io
from PIL import Image

# A list of MIME types that are supported by the QARequest class.
SUPPORTED_MIMETYPES = ["application/pdf", "image/png", "image/jpeg"]

class QARequest:
    
    # The __init__ method initializes the instance variables of the class.
    def __init__(self, bytes, mimetype, query) -> None:
        self.query = query  # The question that the user is asking.
        self.bytes = bytes  # The bytes of the file or image that contains the information relevant to the question.
        self.mimetype = mimetype  # The MIME type of the file or image.
        
        # The MD5 hash of the file or image bytes, which can be used for identification purposes.
        self.hash = md5(bytes).hexdigest()
        
        # Raise a FileIsNotSupported exception if the file or image MIME type is not in the SUPPORTED_MIMETYPES list.
        if not self.mimetype in SUPPORTED_MIMETYPES:
            raise FileIsNotSupported()

    # This class method creates a QARequest object from a file path.
    @classmethod
    def from_file(cls, file, query):
        mime = mimetypes.guess_type(file)[0]  # Guess the MIME type of the file.
        with open(file, "rb") as f:
            return cls(f.read(), mime, query)

    # This class method creates a QARequest object from a URL.
    @classmethod
    def from_url(cls, url, query):
        mime = mimetypes.guess_type(url)[0]  # Guess the MIME type of the URL.
        return cls(requests.get(url).content, mime, query)

    # This class method creates a QARequest object from bytes.
    @classmethod
    def from_bytes(cls, bytes, mimetype, query):
        return cls(bytes, mimetype, query)

    # This class method creates a QARequest object from a PIL Image object.
    @classmethod
    def from_pil_image(cls, image, query):
        imgByteArr = io.BytesIO()
        image.save(imgByteArr, format='JPEG')
        imgByteArr = imgByteArr.getvalue()
        return cls(imgByteArr, "image/jpeg", query)

    # The __str__ method returns a string that represents the object in a readable format.
    def __str__(self) -> str:
        return f"QARequest({self.hash}, {self.mimetype}, {self.query})"