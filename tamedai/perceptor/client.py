import os
from tamedai.perceptor.exceptions import *
import requests
from tamedai.perceptor.request import QARequest
import time
from tamedai.perceptor.response import QAResponse

class PerceptorAPIClient:
    
    # The __init__ method initializes the instance variables of the class.
    def __init__(self, token, api_url="https://perceptor-api.tamed.ai") -> None:
        self.token = token  # The authentication token that is used to access the system.
        self.api_url = api_url  # The URL of the system.
        
    # This method uploads the request to the system, waits for the response, and returns a QAResponse object.
    def run(self, req, temperature=.7, top_k=50, top_p=.9, max_length=128, timeout=60):
        
        # Raise a RequestIsNotValid exception if the input request is not an instance of the QARequest class.
        if not isinstance(req, QARequest):
            raise RequestIsNotValid()
        
        # Create a file object from the request data and upload it to the system using the requests.post method (using multipart/form-data encoding)
        filename = req.hash + "." + req.mimetype.split("/")[1]
        files = [("files", (filename, req.bytes, req.mimetype))]
        header = {"Authorization": f"Bearer {self.token}"}
        url_params = {"query": req.query, "temperature": temperature, "top_k": top_k, "top_p": top_p, "max_length": max_length}
        r = requests.post(f"{self.api_url}/tasks/qa", files=files, headers=header, params=url_params)
        
        # Raise a PerceptorAPIException exception if the HTTP status code is not 200.
        if r.status_code != 200:
            raise PerceptorAPIException(r.json()["detail"])

        # Wait for the response from the system by making repeated GET requests using the requests.get method (using the task ID returned by the POST request)
        # The loop will terminate when the result or error fields of the response are not None. The request ist scheduled by the compute engine depending in the hardware resources available.
        result, error = None, None
        start = time.time()
        while result is None and error is None:
            if time.time() - start > timeout:
                raise TimeoutError()
            time.sleep(.1)
            resp = requests.get(f"{self.api_url}/tasks/qa/{r.json()['id']}", headers=header).json()
            result = resp.get("result")
            error = resp.get("error")

        # Raise a PerceptorAPIException exception if the response contains an error.
        if error is not None:
            raise PerceptorAPIException(error)

        # Create a QAResponse object from the result and return it.
        return QAResponse(result["text"], result["score"])

