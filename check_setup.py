from src.base.api_client import BaseClient

client = BaseClient(base_url="https://jsonplaceholder.typicode.com")

#test Get 
print("----testing get method")
response = client.get("/users", params={"_limit": 3})
print(f"Status Code: {response.status_code}")
print(f"Response JSON: {response.json()[0]['email']}")

print("\n Testing Post")
new_user = {"title": "foo", "body": "bar", "userId": 1}
post_response = client.post(endpoint="/posts", data=new_user)
print(f"Status Code: {post_response.status_code}")
print(f"created Post ID: {post_response.json()['id']}")
