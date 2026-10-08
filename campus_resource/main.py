def display_menu():
    print("\n========================================")
    print(" CAMPUS RESOURCE MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Add Resource")
    print("2. List Resources")
    print("3. Borrow Resource")
    print("4. Return Resource")
    print("5. Search Resources")
    print("6. Filter by Category")
    print("7. Generate Report")
    print("8. Exit")

from .add_resource import add_resource
from .list_resources import list_resources


def handle_add_resource():
    print("\n--- ADD NEW RESOURCE ---")

    resource_id = input("Resource ID: ").strip()
    name = input("Resource Name: ").strip()
    category = input("Category: ").strip()

    try:
        total = int(input("Total Units: "))
        available = int(input("Available Units: "))

    except ValueError:
        print("ERROR: Units must be valid integers.")
        return

    new_resource = {
        "id": resource_id,
        "name": name,
        "category": category,
        "total": total,
        "available": available
    }

    try:
        add_resource(new_resource)

    except ValueError as error:
        print(f"ERROR: {error}")

    else:
        print(f"SUCCESS: {name} added to inventory.")

def main():
    while True:
        display_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            handle_add_resource()

        elif choice == "2":
            list_resources()

        elif choice == "3":
            print("Borrow Resource selected")

        elif choice == "4":
            print("Return Resource selected")

        elif choice == "5":
            print("Search Resources selected")

        elif choice == "6":
            print("Filter by Category selected")

        elif choice == "7":
            print("Generate Report selected")

        elif choice == "8":
            print("Exiting Campus Resource Management System...")
            break

        else:
            print("Invalid choice. Please select 1 to 8.")


if __name__ == "__main__":
    main()          