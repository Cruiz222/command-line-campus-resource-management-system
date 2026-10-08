from .add_resource import add_resource
from .find_resource import find_resource


def test_add_valid_resource():
    new_resource = {
        "id": "R004",
        "name": "Mouse",
        "category": "Accessories",
        "total": 5,
        "available": 5
    }

    add_resource(new_resource)

    saved_resource = find_resource("R004")

    assert saved_resource is not None
    assert saved_resource["name"] == "Mouse"
    assert saved_resource["total"] == 5
    assert saved_resource["available"] == 5

if __name__ == "__main__":
    test_add_valid_resource()
    print("PASS: Valid resource added successfully")