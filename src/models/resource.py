class Resource:
    def __init__(self, resource_id: str, name: str):
        self.resource_id = resource_id
        self.name = name
        self.access_types = set()

    def add_access_type(self, access_type):
        self.access_types.add(access_type)

    def __str__(self):
        return f"Resource(id={self.resource_id}, name={self.name})"