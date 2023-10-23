def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Command not recognized."

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(contacts, name, phone):
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError


@input_error
def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError


@input_error
def show_all(contacts):
    if not contacts:
        raise ValueError
    result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return result


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Give me name and phone please.")
            else:
                name, phone = args
                print(add_contact(contacts, name, phone))
        elif command == "change":
            if len(args) != 2:
                print("Give me name and phone please.")
            else:
                name, phone = args
                print(change_contact(contacts, name, phone))
        elif command == "phone":
            if len(args) != 1:
                print("Enter user name.")
            else:
                name = args[0]
                print(show_phone(contacts, name))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Command not recognized.")


if __name__ == "__main__":
    main()
