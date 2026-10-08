from .campus_resource import fellows

def borrow_resource(fellow_id, resource_id, quantity):
    if fellow_id not in fellows:
        raise ValueError(f"Fellow ID {fellow_id} does not exist.")

    resource = find_resource(resource_id)

    if resource is None:
        raise ValueError(f"Resource ID {resource_id} does not exist.")

    validate_quantity(quantity)

    if quantity > resource["available"]:
        raise ValueError(
            f"Insufficient stock. Only {resource['available']} "
            "unit(s) available."
        )

    resource["available"] -= quantity

    borrow_records.append({
        "fellow_id": fellow_id,
        "resource_id": resource_id,
        "quantity": quantity
    })

    print(
        f"SUCCESS: {fellows[fellow_id]} borrowed "
        f"{quantity} {resource['name']}(s)."
    )
    print(f"Available {resource['name']} units: {resource['available']}")
