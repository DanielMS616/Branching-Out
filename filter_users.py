import json


def load_users(filename):
    """Load user data from a JSON file.
    Returns an empty list if the file is missing, or it contains invalid JSON.
    """

    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"Error: {filename} was not found.")
        return []

    except json.JSONDecodeError:
        print(f"Error: {filename} does not contain valid JSON.")
        return []


def filter_users_by_name(users, name):
    return [user for user in users if user["name"].lower() == name.lower()]


def filter_users_by_age(users, minimum_age):
    return [user for user in users if user["age"] >= minimum_age]


def filter_users_by_email(users, email):
    return [user for user in users if user["email"].lower() == email.lower()]


def print_users(users):
    """Print matching users or show a message if no users were found."""

    if not users:
        print("No matching users found.")
        return

    for user in users:
        print(user)


def get_minimum_age():
    """Ask the user for a minimum age and validate the input.
    Returns the age as an integer if valid.
    Returns None if the input is not a whole number or is negative.
    """

    age_input = input("Enter minimum age: ").strip()

    try:
        age = int(age_input)

    except ValueError:
        print("Error: Age must be a whole number.")
        return None

    if age < 0:
        print("Error: Age must not be negative.")
        return None

    return age


def main():
    """Run the user filtering program.
    Loads user data, asks for a filter option, validates user input,
    applies the selected filter, and prints the result.
    """

    users = load_users("users.json")

    if not users:
        return

    filter_option = input(
        "What would you like to filter by? ('name', 'age' or 'email'): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()

        if not name_to_search:
            print("Error: Name must not be empty.")
            return

        filtered_users = filter_users_by_name(users, name_to_search)

    elif filter_option == "age":
        age_to_search = get_minimum_age()

        if age_to_search is None:
            return

        filtered_users = filter_users_by_age(users, age_to_search)

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()

        if not email_to_search:
            print("Error: Email must not be empty.")
            return

        filtered_users = filter_users_by_email(users, email_to_search)

    else:
        print("Filtering by that option is not yet supported.")
        return

    print_users(filtered_users)


if __name__ == "__main__":
    main()
