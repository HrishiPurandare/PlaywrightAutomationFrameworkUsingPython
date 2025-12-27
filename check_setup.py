from src.services.user_client import UserClient

# 1. Initialize the Service (No need to pass URL anymore, the class knows it)
api = UserClient()

# 2. Test: Get Specific User
print("--- Fetching User ID 1 ---")
response = api.get_user_by_id(user_id=1)
user_email = response.json()['email']
print(f"User Found: {user_email}")

# 3. Test: Create User
print("\n--- Creating New User ---")
# See how clean this is? No dictionaries, just arguments.
post_response = api.create_user(name="Hrishikesh", job="Automation Architect")
print(f"Status: {post_response.status_code}")
print(f"Created ID: {post_response.json()['id']}")