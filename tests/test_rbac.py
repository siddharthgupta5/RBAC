import pytest
from src.core.rbac_system import RBACSystem
from src.models.access_type import AccessType

@pytest.fixture
def rbac_system():
    return RBACSystem()

def test_add_user(rbac_system):
    assert rbac_system.add_user("user1", "Sid Gupta")
    assert "user1" in rbac_system.users
    assert not rbac_system.add_user("user1", "Sid Gupta")  

def test_add_role(rbac_system):
    assert rbac_system.add_role("role1", "Admin")
    assert "role1" in rbac_system.roles
    assert not rbac_system.add_role("role1", "Admin")  

def test_add_resource(rbac_system):
    assert rbac_system.add_resource("res1", "File1")
    assert "res1" in rbac_system.resources
    assert not rbac_system.add_resource("res1", "File1")  

def test_assign_role_to_user(rbac_system):
    rbac_system.add_user("user1", "Sid Gupta")
    rbac_system.add_role("role1", "Admin")
    assert rbac_system.assign_role_to_user("user1", "role1")
    assert "role1" in rbac_system.users["user1"].roles

def test_permission_checking(rbac_system):
    
    rbac_system.add_user("user1", "Sid Gupta")
    rbac_system.add_role("role1", "Admin")
    rbac_system.add_resource("res1", "File1")
    rbac_system.assign_role_to_user("user1", "role1")
    rbac_system.assign_permission_to_role("role1", "res1", AccessType.READ)
    
    
    assert rbac_system.check_permission("user1", "res1", AccessType.READ)
    assert not rbac_system.check_permission("user1", "res1", AccessType.WRITE)