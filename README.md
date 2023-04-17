# 🤖 PERCEPTOR API Client
This repository contains an API client for the PERCEPTOR Model of TamedAI. PERCEPTOR is a large language model designed to extract information from business document images. This API client provides a Python interface for interacting with the PERCEPTOR API to perform tasks like question-answering and information extraction from document images.

## 📦 Installation
To install the PERCEPTOR API Client, run the following command:

```bash
pip install git+https://github.com/TamedAI/perceptor-client-python
```

First, you need to import the necessary classes and functions:

```python
from tamedai.perceptor import QARequest, PerceptorAPIClient
```

Then, create an instance of the API client by passing your API token:

```python
client = PerceptorAPIClient("Your token here")
```
You can now create a QARequest object by providing a URL of an image and a query:

```python
req = QARequest.from_url("https://your_url_here", "Your query here?")

#req=QARequest.from_file...
#req=QARequest.from_bytes...
#req=QARequest.from_pil_image...
```


To get the answer, run the request using the client:

```python
res = client.run(req)
```
You can then access the response text and score as follows:

```python
print(f"""
    Request: {req.query}
    Response: {res.text}
    Score: {res.score}
""")
```

## 📚 Example
Here's a full example of using the PERCEPTOR API client to extract information from a document image:

```python
from tamedai.perceptor import QARequest, PerceptorAPIClient
import argparse

if __name__=="__main__":

    args = argparse.ArgumentParser()
    args.add_argument("--token", type=str, required=True)

    args = args.parse_args()

    client = PerceptorAPIClient(args.token)

    print("####### Run example #######")

    req = QARequest.from_url("https://datasets-server.huggingface.co/assets/rvl_cdip/--/default/train/95/image/image.jpg", "Von welchem Datum ist der Brief?")

    res = client.run(req)

    print(
        f"""
        Request: {req.query}
        Response: {res.text}
        Score: {res.score}
        """
    )
```

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.
