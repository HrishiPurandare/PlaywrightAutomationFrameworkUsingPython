import requests
from typing import Any, Dict

class BaseClient:
    def __init__(self, base_url: str):
        """
        The Constructor.
        :param base_url: The root URL for the API (e.g., 'https://reqres.in')
        """
        self.base_url = base_url
        self.session = requests.Session() # Session manages cookies/headers efficiently

    def _get_headers(self) -> Dict[str, str]:
        """
        Private method to generate headers. 
        Architect Note: Centralize header logic here (Auth tokens, Content-Type).
        """
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        }

    def get(self, endpoint: str, params: Dict[str, Any] = None) -> requests.Response:
        """
        Generic GET method.
        :param endpoint: The specific path (e.g., '/api/users')
        :param params: URL parameters (e.g., {'page': 2})
        """
        url = f"{self.base_url}{endpoint}"
        print(f"Testing GET: {url}") # Simple logging for now
        
        try:
            response = self.session.get(url, headers=self._get_headers(), params=params)
            response.raise_for_status() # Raise error if status is 4xx or 5xx
            return response
        except requests.exceptions.RequestException as e:
            print(f"GET Request Failed: {e}")
            raise # Re-raise the error so the test knows it failed

    def post(self, endpoint: str, data: Dict[str, Any]) -> requests.Response:
        """
        Generic POST method.
        """
        url = f"{self.base_url}{endpoint}"
        print(f"Testing POST: {url}")
        
        try:
            response = self.session.post(url, headers=self._get_headers(), json=data)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"POST Request Failed: {e}")
            raise