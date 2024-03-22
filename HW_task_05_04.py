#Декоратори
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return " IndexError Enter the argument for the command."
        except KeyError:
            return " KeyError Enter the argument for the command."

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
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."
@input_error
def all_contact(contacts):
    line = "|{:^15}|{:^15}|".format("name", "phone")
    separator = "_"*len(line)
    body = ""
    for key, val in contacts.items():
        body += ("|{:<15}|{:>15}|\n".format(key, val))
    table = "\n".join([separator, line, separator, body, separator])
    return table

@input_error
def phone_username(args, contacts):
    name, *_ = args
    return contacts[name]
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        # "hello"відповідає у консоль повідомленням "How can I help you?"
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts))
        elif command == "all":
            print(all_contact(contacts))
        else:
            print("Invalid command.")
if __name__ == "__main__":
    main()