from aquilapy import Wallet, DB, Hub
from bs4 import BeautifulSoup
import urllib.request
import sys

# Create a wallet instance from private key
wallet = Wallet("/Users/jubinjose/works/aquila_network/pems/DO/private_unencrypted.pem")

host = "http://167.71.229.127"

# Connect to Aquila DB instance
db = DB(host, "5001", wallet)

# Connect to Aquila Hub instance
hub = Hub(host, "5002", wallet)

# Schema definition to be used
schema_def = {
    "description": "Wikipedia",
    "unique": "243190",
    "encoder": "ftxt:https://ftxt-models.s3.us-east-2.amazonaws.com/wiki_100d_en.bin",
    "codelen": 100,
    "metadata": {
        "url": "string",
        "text": "string"
    }
}


# Craete a database with the schema definition provided
db_name = db.create_database(schema_def)

# Craete a database with the schema definition provided
db_name_ = hub.create_database(schema_def)


    


# Compress data
def compress_strings (db_name, strings_in):
    return hub.compress_documents(db_name, strings_in)

# Insert docs
def index_a_url (db_name, url):
    paragraphs = get_paragraphs(url)
    compressed = compress_strings(db_name, paragraphs)
    docs = []
    for idx_, para in enumerate(paragraphs):
        docs.append({
            "metadata": {
                "url": url, 
                "text": para
            },
            "code": compressed[idx_]
        })
    dids = db.insert_documents(db_name, docs)

# Search docs
def search(db_name, query):
    compressed = compress_strings(db_name, [query])
    docs, dists = db.search_k_documents(db_name, compressed, 100)
    index = {}
    score = {}
    for idx_, doc in enumerate(docs[0]):
        metadata = doc["metadata"]
        if index.get(metadata["url"]):
            index[metadata["url"]] += 1
            score[metadata["url"]] += dists[0][idx_]
        else:
            index[metadata["url"]] = 1
            score[metadata["url"]] = dists[0][idx_]

    results_d = {}
    for key in index:
        results_d[key] = round(index[key] * score[key])

    results_d = {k: v for k, v in sorted(results_d.items(), key=lambda item: item[1], reverse=True)}
    
    # threshold = -1
    for key in results_d:
        print(key, results_d[key])
    #     if threshold == -1:
    #         threshold = round(results_d[key]*0.1)
    #     if results_d[key] > threshold:
    #         print(key)

# Get HTML text from url
def get_html(url):
    fp = urllib.request.urlopen(url)
    data = fp.read()
    fp.close()
    return data.decode("utf8")

# Get paragraphs given url
def get_paragraphs(url):
    html_doc = get_html(url)
    soup = BeautifulSoup(html_doc, 'html.parser')
    paras = []
    for para in soup.find_all("p"):
        text_data = para.text
        for txt in text_data.split("\n"):
            if txt.strip() != "":
                paras.append(" ".join(txt.strip().split()))
    return paras


# Parse arguments
command_arg = None
arg_arg = None
if len(sys.argv) >= 3:
    command_arg = sys.argv[1]
    arg_arg = " ".join(sys.argv[2:])
else:
    print("1 Usage: python3 web_test <command> <argument>")
    exit()

if command_arg != "index" and command_arg != "search":
    print("2 Usage: python3 web_test <command> <argument>")
    exit()


# Index a url
if command_arg == "index":
    with open(arg_arg) as fp:
        urls = fp.read()
        for url in urls.split("\n"):
            print("indexing: "+url)
            index_a_url(db_name, url)

# Search database
if command_arg == "search":
    print("Searching: "+arg_arg)
    search(db_name, arg_arg)