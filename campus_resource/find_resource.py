from .campus_resource import resources

def find_resource(resource_id: str) -> dict | None:
    for resource in resources:
        if resource["id"] == resource_id:
            return resource

    return None