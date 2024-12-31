from ..core.rbac_system import RBACSystem
from ..models.access_type import AccessType

class CommandLineInterface:
    def __init__(self, rbac_system: RBACSystem):
        self.rbac = rbac_system
        self.commands = {
            "add_user": self.add_user,
            "add_role": self.add_role,
            "add_resource": self.add_resource,
            "assign_role": self.assign_role,
            "assign_permission": self.assign_permission,
            "check_permission": self.check_permission,
            "help": self.show_help,
            "exit": self.exit_cli
        }
        self.running = True

    def run(self):
        print("Welcome to RBAC System. Type 'help' for available commands.")
        while self.running:
            try:
                command = input("> ").strip()
                if not command:
                    continue
                
                parts = command.split()
                cmd = parts[0].lower()
                args = parts[1:]

                if cmd in self.commands:
                    self.commands[cmd](*args)
                else:
                    print(f"Unknown command: {cmd}")
            except Exception as e:
                print(f"Error: {str(e)}")

    def add_user(self, user_id: str, name: str):
        if self.rbac.add_user(user_id, name):
            print(f"User {name} ({user_id}) added successfully")
        else:
            print(f"Failed to add user: {user_id} already exists")

    def add_role(self, role_id: str, name: str):
        if self.rbac.add_role(role_id, name):
            print(f"Role {name} ({role_id}) added successfully")
        else:
            print(f"Failed to add role: {role_id} already exists")

    def add_resource(self, resource_id: str, name: str):
        if self.rbac.add_resource(resource_id, name):
            print(f"Resource {name} ({resource_id}) added successfully")
        else:
            print(f"Failed to add resource: {resource_id} already exists")

    def assign_role(self, user_id: str, role_id: str):
        self.rbac.assign_role_to_user(user_id, role_id)
        self.rbac.assign_role_to_user(user_id, role_id)
        print(f"Role {role_id} assigned to user {user_id}")


    def assign_permission(self, role_id: str, resource_id: str, access_type: str):
        try:
            access = AccessType(access_type.lower())
            self.rbac.assign_permission_to_role(role_id, resource_id, access)
            print(f"Permission {access_type} on {resource_id} assigned to role {role_id}")
        except ValueError:
            print(f"Invalid access type: {access_type}")

    def check_permission(self, user_id: str, resource_id: str, access_type: str):
        try:
            access = AccessType(access_type.lower())
            if self.rbac.check_permission(user_id, resource_id, access):
                print("Permission granted")
            else:
                print("Permission denied")
        except ValueError:
            print(f"Invalid access type: {access_type}")


    def show_help(self):
        print("\nAvailable commands:")
        print("add_user <user_id> <name>")
        print("add_role <role_id> <name>")
        print("add_resource <resource_id> <name>")
        print("assign_role <user_id> <role_id>")
        print("assign_permission <role_id> <resource_id> <access_type>")
        print("check_permission <user_id> <resource_id> <access_type>")
        print("help")
        print("exit\n")

    def exit_cli(self):
        print("Bye!")
        self.running = False