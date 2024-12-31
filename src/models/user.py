
class User:
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.roles = set()

    def add_role(self, role_id: str):
        self.roles.add(role_id)

    def __str__(self):
        return f"User(id={self.user_id}, name={self.name})"
