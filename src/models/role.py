

class Role:
    def __init__(self, role_id: str, name: str):
        self.role_id = role_id
        self.name = name
        self.permissions = {}  

    def add_permission(self, resource_id: str, access_type):
        if resource_id not in self.permissions:
            self.permissions[resource_id] = set()
        self.permissions[resource_id].add(access_type)

    def has_permission(self, resource_id: str, access_type) -> bool:
        return (resource_id in self.permissions and 
                access_type in self.permissions[resource_id])

    def __str__(self):
        return f"Role(id={self.role_id}, name={self.name})"