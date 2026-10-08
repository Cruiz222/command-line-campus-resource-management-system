from .find_resource import find_resource
from .campus_resource import resources

def add_resource(new_resource: dict) -> None:
    resource_id = new_resource["id"]

    existing_resource_id = find_resource(resource_id)

    if existing_resource_id is not None:
        raise ValueError(
            f"Resource ID {resource_id} already exists"
        )

    if new_resource["total"] < 0:
        raise ValueError(
            "total resources can not be negative"
        )

    if new_resource["available"] > new_resource["total"]:
        raise ValueError(
            "total resources must be more or equal to available resources"
        )

    resources.append(new_resource)    