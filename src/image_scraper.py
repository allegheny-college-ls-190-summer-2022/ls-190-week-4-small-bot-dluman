import requests
import random
import json

def load_keys():
    """Load keys file"""
    # Find the file and open it
    file = open("../.secrets/keys.json")
    # Parse JSON
    keys = json.load(file)
    # Return results
    return keys

keys = load_keys()
# This key only lives on jupyter.cs.allegheny.edu
api_access = keys["UNSPLASH_ACCESS"]
page = 1

#               DOMAIN          |----API------| |-----------PARAMETERS----------------|
url = f"https://api.unsplash.com/search/photos/?client_id={api_access}&query=dinosaur&page={page}"

response = requests.get(url)
data = json.loads(response.content)

total = data["total"]
pages = data["total_pages"]

results = []
for page in range(pages):
    url = f"https://api.unsplash.com/search/photos/?client_id={api_access}&query=dinosaur&page={page}"
    response = requests.get(url)
    results.append(response["results"])
    
print(random.choice(results))