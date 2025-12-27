from src.base.api_client import BaseClient

class UserClient(BaseClient):
    def __init__(self):
        # We call the Parent's constructor (super) to set up the session
        # Note: We are hardcoding the URL here for today. Tomorrow we move it to Config.
        super().__init__(base_url="https://jsonplaceholder.typicode.com")

    def get_all_users(self):
        """
        Business Logic: Fetch all users.
        The test doesn't need to know the endpoint is '/users'.
        """
        return self.get(endpoint="/users")

    def get_user_by_id(self, user_id: int):
        """
        Fetch a single user.
        """
        return self.get(endpoint=f"/users/{user_id}")

    def create_user(self, name: str, job: str):
        """
        Create a user with specific payload structure.
        """
        payload = {
            "name": name,
            "username": name, # Just using name as username for demo
            "company": {
                "name": job
            }
        }
        return self.post(endpoint="/users", data=payload)