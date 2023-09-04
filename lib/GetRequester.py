import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        json_data = json.loads(self.get_response_body())
        json_dump = json.dumps(json_data, indent=4, sort_keys=True)
        return json_data

