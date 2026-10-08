from .campus_resource import resources


def list_resources() -> None:
    print("\n--- RESOURCE INVENTORY ---")

    for resource in resources:
        resource_id = resource["id"]
        name = resource["name"]
        category = resource["category"]
        total = resource["total"]
        available = resource["available"]

        print(
            f"{resource_id:<8}"
            f"{name:<15}"
            f"{category:<18}"
            f"{total:<10}"
            f"{available:<10}"
        )