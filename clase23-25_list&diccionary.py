import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Sofware Engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer',
    },
    {
        'name': 'Junior',
        'company': 'Bitel',
        'email': 'juniorpeves@gmail.com',
        'position': 'Electrónico',
    }
]
def _get_client_field(field_name):
    field = None
    while not field:
        field = input('What is the client {}?'.format(field_name))
    return field
def _get_client_name():
    client_name = None
    ## 19. While loops
    while not client_name:
        client_name = input('What is the client name? ').strip()
        if client_name == 'exit':
            client_name = None
            break
    if not client_name:
        sys.exit()
    return client_name        

def create_client(client):
	global clients  
	if client not in clients:
		clients.append(client)
	else:
		print('Client already exists')

def update_client(client_name):
    for idx, client in enumerate(clients):
        if client_name == client['name']:
            clients.pop(idx)
            clients.append(input_client())
            break
        
def delete_client(client_name):
    global clients
    for idx, client in enumerate(clients):
        if client_name == client['name']:
            clients.pop(idx)
        else:
            print('Client isD not clients list')  

def search_client(client_name):
    ## 18. For loops
    for client in clients:
        if client != client_name:
            continue
        else:
            return True
def input_client():
    client={
            'name': _get_client_field('name'),
            'company':_get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
            }
    return client
    
        
def list_clients(): 
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid =idx, 
            name =client['name'],
            company = client['company'],
            email =client['email'],
            position =client['position']))
def _add_coma():  
	global clients
	clients +=", "

def _print_welcome():
    print ('Welcome to Monares POS')
    print ('*' * 52)
    print ('what would you like to do today?')
    print ('[C]reate client')
    print ('[L]ist client')
    print ('[S]earch client')
    print ('[D]elete client')
    print ('[U]pdate client')

if __name__ == '__main__':
    _print_welcome()
    command = input().lower()
    if command == 'c':
        create_client(input_client())
        list_clients()
    elif command == 'l':
            list_clients()
    elif command == 'u':
        client_name = input('What is the client name? ').strip()
        update_client(client_name)
        list_clients()
    elif command == 'd':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 's':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print(f'The client {client_name} i not in our client\'s list')
    else:
        print('Invalid command')

input()
