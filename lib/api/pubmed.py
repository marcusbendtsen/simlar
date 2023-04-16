import requests
import xmltodict

endpoints = {
    "search" : "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
    "fetch"  : "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
}

def search(terms):

    data = {
        "term" : terms,
        "db" : "pubmed",
        "retmax" : 1000000
    }
    
    r = requests.post(url = endpoints["search"], data = data)
    results = xmltodict.parse(r.text)
    results = results["eSearchResult"]
    ids = results["IdList"]["Id"]
    return ids

def fetch(ids, rettype = "XML"):

    if not type(ids) is list: ids = [ids]
    
    data = {
        "id" : ",".join(ids),
        "db" : "pubmed",
        "retmax" : 1000000,
        "rettype" : rettype
    }
    
    r = requests.post(url = endpoints["fetch"], data = data)
    return r.text


def xml_to_dict(data):
    data = xmltodict.parse(data)
    data = data["PubmedArticleSet"]["PubmedArticle"]
    return data




