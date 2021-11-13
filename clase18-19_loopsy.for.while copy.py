import sys

clients = 'Carlos, Javier, Carminha, Eliana' #creamos el string

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

def create_client(client_name):
	global clients  
	clients_minusculas = clients.lower()
	if client_name.lower() not in clients_minusculas:
		_add_coma() 
		clients += client_name  
	else:
		print('Client already exists')

def update_client(client_name, updated_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name+',',updated_client_name+',')
    else:
        print('Client is not clients list')

def delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name+',','')
    else:
        print('Client is not clients list')

def search_client(client_name):
    clients_list = clients.split(', ')
    ## 18. For loops
    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True
        
def list_clients(): 
	global clients
	print (clients) 

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
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'l':
            list_clients()
    elif command == 'u':
        client_name = _get_client_name()
        updated_client_name = input('What is the update client name? ').lower()
        update_client(client_name, updated_client_name)
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
