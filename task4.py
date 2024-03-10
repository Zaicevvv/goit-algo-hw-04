def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            return f'Contact "{name}" already exists. To change it use command "change"'
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return 'Invalid format! Use "add <name> <phone>'
    
def change_contact(args, contacts):
    try:
        name, phone = args
        if name not in contacts:
            return f"Contact '{name}' doesn't exists. To add it use command 'add'"
        contacts[name] = phone
        return "Contact changed."
    except ValueError:
        return 'Invalid format! Use "change <name> <new phone>'
    
def show_phone(args, contacts):
    return f'name: {args[0]}, phone: {contacts[args[0]]}'
    
def show_all(contacts):
    show = ''
    for name, phone in sorted(contacts.items()):
        show += f'name: {name}, phone: {phone}\n'
    return show.strip()

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
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()