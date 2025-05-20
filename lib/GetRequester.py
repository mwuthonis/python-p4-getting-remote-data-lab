import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        try:
            return json.loads(response_body)
        except json.JSONDecodeError:
            print("Error decoding JSON")
            return None

if __name__ == "__main__":
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    get_requester = GetRequester(url)

    print("Raw Response Body:\n", get_requester.get_response_body())
    print("\nParsed JSON:\n", get_requester.load_json())
