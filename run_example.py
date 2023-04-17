from tamedai.perceptor import QARequest, PerceptorAPIClient
import argparse

if __name__=="__main__":

    args=argparse.ArgumentParser()
    args.add_argument("--token",type=str,required=True)

    args=args.parse_args()

    client = PerceptorAPIClient(args.token)

    print("####### Running first example #######")

    req=QARequest.from_url("https://datasets-server.huggingface.co/assets/rvl_cdip/--/default/train/95/image/image.jpg","Von welchem Datum ist der Brief?")

    res=client.run(req)
    
    print(
        f"""
        Request: {req.query}
        Response: {res.text}
        Score: {res.score}
        """
    )

    print("####### Running second example #######")

    req=QARequest.from_url("https://datasets-server.huggingface.co/assets/rvl_cdip/--/default/train/58/image/image.jpg","Über welche Rufnummer kann man sich einwählen?")

    res=client.run(req)
    
    print(
        f"""
        Request: {req.query}
        Response: {res.text}
        Score: {res.score}
        """
    )

    print("####### Running third example #######")

    req=QARequest.from_url("https://datasets-server.huggingface.co/assets/rvl_cdip/--/default/train/66/image/image.jpg","Wie hoch ist die Rechnungssumme?")

    res=client.run(req)
    
    print(
        f"""
        Request: {req.query}
        Response: {res.text}
        Score: {res.score}
        """
    )

    print("####### Running fourth example #######")

    req=QARequest.from_url("https://datasets-server.huggingface.co/assets/rvl_cdip/--/default/train/77/image/image.jpg","Aus welchem Jahr ist der Artikel?")

    res=client.run(req)
    
    print(
        f"""
        Request: {req.query}
        Response: {res.text}
        Score: {res.score}
        """
    )

    print("####### Running fifth example #######")

    req=QARequest.from_url("https://datasets-server.huggingface.co/assets/rvl_cdip/--/default/train/2/image/image.jpg","Wie lautet die Adresse des Zahlungsempfängers?")

    res=client.run(req)
    
    print(
        f"""
        Request: {req.query}
        Response: {res.text}
        Score: {res.score}
        """
    )

    print("####### Running sixth example #######")

    req=QARequest.from_url("https://datasets-server.huggingface.co/assets/rvl_cdip/--/default/train/0/image/image.jpg","Wie lautet die Rechnungsnummer?")

    res=client.run(req)
    
    print(
        f"""
        Request: {req.query}
        Response: {res.text}
        Score: {res.score}
        """
    )