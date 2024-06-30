# Define the necessary functions.

# Parse the string entered by the user into a command and its arguments.
def parse_input(user_input: str):
    # Arguments may consist of username, phone.
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, *args

# The function adds or change the contact.
def add_or_change_contact(name: str, phone: str, contacts: dict):
    contacts[name] = phone

# The function show a phone number.
def show_phone(name: str, contacts: dict) -> str:
    return contacts[name]



def main():
    # Create dictionary of contacts.
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        # Print "Menu".
        print('Please select one of the following commands.\n\
              - Input "Hello" to greet the assistant!\n\
              - Input "add [username] [phone]" to add "username" and their "phone" to the contacts.\n\
              - Input "change [username] [phone]" to change the "phone" of the "username.\n\
              - Input "phone [username]" to print the "phone" of the "username".\n\
              - Input "all" to print all saved contacts.\n\
              - If you want to complete the work with the assistant, then input "close" or "exit".')
        user_input = input('Enter a command: ')
        # Parse the string entered by the user into a command and its arguments.
        command, *args = parse_input(user_input) 

        # Create dictionary of args.
        dict_args = {'name': ''}
        for arg in args:
            if arg.isdecimal():
                dict_args['phone'] = arg
            elif arg.isalnum(): 
                dict_args['name'] += arg + ' '
        dict_args['name'] = dict_args['name'].strip()

        # React to the command.
        match command:

            # Input "Hello" to greet the assistant!
            case 'hello':
                print('How can I help you?')
            
            # Input "add [username] [phone]" to add "username" and their "phone" to the contacts.
            case 'add':
                try:
                    # Check the presence of a contact.
                    if contacts.get(dict_args['name']):
                        print('Such contact already exists.')
                    else:
                        add_or_change_contact(dict_args['name'], dict_args['phone'], contacts)
                        print(f'Contact added: {dict_args}.')
                except KeyError:
                    print('Error. Contact was not added.')
            
            # Input "change [username] [phone]" to change the "phone" of the "username.
            case 'change':
                try:
                    # Check the presence of a contact.
                    if not contacts.get(dict_args['name']):
                        print('No such contact exists.')
                    else:
                        add_or_change_contact(dict_args['name'], dict_args['phone'], contacts)
                        print(f'Contact changed: {dict_args}.')
                except KeyError:
                    print('Error. Contact was not changed.')

            # Input "phone [username]" to print the "phone" of the "username".
            case 'phone':
                try:
                    print(show_phone(dict_args['name'], contacts))
                except KeyError:
                    print('No contact.')
            
            # Input "all" to print all saved contacts.
            case 'all':
                print(contacts)
            
            # If you want to complete the work with the assistant, then input "close" or "exit".
            case 'close' | 'exit':
                print('Good bye!')
                break
            
            # Another case.
            case _:
                print('Invalid command.')

if __name__ == '__main__':
    main()
