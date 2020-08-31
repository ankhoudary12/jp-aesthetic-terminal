import requests

API_URL = "https://ja.wikipedia.org/api/rest_v1/page/random/summary"

with requests.get(API_URL) as response:
    response.raise_for_status()

    data = response.json()

    extract = data["extract"].split("、")

    print(extract)
