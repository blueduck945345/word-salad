'''Client for Word Salad API'''
import requests

class WordSaladClientException(Exception):
    pass

class WordSaladClient:
    def __init__(self, base_url: str = 'http://127.0.0.1:8000'):
        self.base_url = base_url

    def make_request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(method, url, **kwargs)
            response.raise_for_status()
        except requests.RequestException as e:
            raise WordSaladClientException(f"Request failed: {e}")
        return response.json()

    def sample(self, size: int) -> list[str]:
        return self.make_request("GET", "sample", params={"size": size})

    def load(self, text: str) -> dict[str, str]:
        return self.make_request("POST", "load", json={"text": text})