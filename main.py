import os
from datetime import datetime
from lib.api import pubmed

topic = "alcohol_cvd"
today = datetime.today().strftime("%Y-%m-%d")

def get_query(topic):
    query = ""
    sep = ""
    for part in topic.split("_"):
        query += sep + "".join(open("query/%s.txt" % part, "r").readlines())
        sep = " AND "
    query = query.replace("\n", "")
    return query


def search_pubmed(query):
    ids = pubmed.search(query)
    if len(ids) == 9999:
        print("Warning: Max items retrieved, may be missing results")
    data = pubmed.fetch(ids, rettype="XML")
    return data
    
    

query = get_query(topic)
data = search_pubmed(query)

directory = "search/%s/%s" % (topic, today)
os.makedirs(directory, exist_ok=True)
with open("%s/raw.xml" %directory, "w") as f:
    f.write(data)

items = pubmed.xml_to_dict(data)
len(items)
items[0]

items[0]["PubmedData"]
items[0]["MedlineCitation"]["Article"]["ArticleTitle"]
