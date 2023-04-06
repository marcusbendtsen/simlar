import requests
import xmltodict

endpoints = {
    "search" : "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
    "fetch"  : "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
}

term = "alcohol and trial"

def search(terms):

    data = {
        "term" : terms,
        "db" : "pubmed",
        "retmax" : 1000000
    }
    r = requests.post(url = endpoints["search"], data = data)  
    results = xmltodict.parse(r.text)
    results = results["eSearchResult"]
    return results["IdList"]["Id"]


def fetch(ids, rettype = "MEDLINE"):

    if not type(ids) is list: ids = [ids]
    
    data = {
        "id" : ",".join(ids),
        "db" : "pubmed",
        "retmax" : 1000000,
        "rettype" : rettype
    }

    r = requests.post(url = endpoint, data = data)
    return r.text


ids = search(term)

print(fetch(ids[0:2])) 

