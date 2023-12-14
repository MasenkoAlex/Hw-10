def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Ther is no contact."
        except IndexError:
            return "Give me a name!"

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change(args, contacts):
    username, phone = args   
    if contacts[username]:
        contacts[username] = phone
    return f"phone number {phone} for {username} has changed" 


def all(args, contacts:dict):
    res = ""
    if not contacts:
        return f"There no conacts!"
    for name, phone in contacts.items():
        res += f"{name}: {phone} \n"
    return res


@input_error
def phone_username(args, contacts:dict):
    username = args[0]
    phone_number = contacts.get(username)
    if phone_number:
        return f"Username {username} has a phone number {phone_number}"
    return f"Contact not found"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change(args, contacts))
        elif command == "all":
            print(all(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
