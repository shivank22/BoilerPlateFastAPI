class UserMetadata:
    class Create:
        summary = "Create a new user"
        description = "Endpoint to register a new user into the system."

user_metadata = UserMetadata()

user_fields = {
    "name": "Full name of the user",
    "email": "Valid email address",
    "age": "Age of the user (must be a positive integer)",
}

user_example = {
    "name": "Alice Doe",
    "email": "alice@example.com",
    "age": 30,
}