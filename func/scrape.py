import requests

def scrape(url: str):
    """
    Docstring for scrape
    
    :param url: Description
    :type url: str

    We are using a function where the requests.get will talk to the url and return back the responses, text and headers and we are initiating a variable and returning responses.text
    """
    responses = requests.get(url)
    source = responses.text

    return source