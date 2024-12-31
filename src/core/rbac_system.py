from typing import Set, Dict
from ..models.user import User
from ..models.role import Role
from ..models.resource import Resource
from ..models.access_type import AccessType

class RBACSystem:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.roles: Dict[str, Role] = {}
        self.resources: Dict[str, Resource] = {}

    def add_user(self, user_id: str, name: str) -> bool:
        if user_id in self.users:
            return False
        self.users[user_id] = User(user_id, name)
        return True

    def add_role(self, role_id: str, name: str) -> bool:
        if role_id in self.roles:
            return False
        self.roles[role_id] = Role(role_id, name)
        return True

    def add_resource(self, resource_id: str, name: str) -> bool:
        if resource_id in self.resources:
            return False
        self.resources[resource_id] = Resource(resource_id, name)
        return True

    def assign_role_to_user(self, user_id: str, role_id: str) -> bool:
        if user_id in self.users:
            self.users[user_id].add_role(role_id)
            return True
    def assign_permission_to_role(self, role_id: str, resource_id: str, access_type: AccessType) -> bool:
        if role_id in self.roles:
            self.roles[role_id].add_permission(resource_id, access_type)
            return True
        return False
        if role_id in self.roles:
            self.roles[role_id].add_permission(resource_id, access_type)

    def check_permission(self, user_id: str, resource_id: str, access_type: AccessType) -> bool:
        if user_id not in self.users or resource_id not in self.resources:
            return False
        
        user = self.users[user_id]
        for role_id in user.roles:
            if role_id in self.roles:
                role = self.roles[role_id]
                if role.has_permission(resource_id, access_type):
                    return True
        return False
