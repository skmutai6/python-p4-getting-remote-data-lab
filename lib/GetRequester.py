import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):        
        response = requests.get('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
        return response.content
 
    def load_json(self):
        pass
