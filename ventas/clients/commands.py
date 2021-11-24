import click
from click.termui import prompt
from clients.services import ClientService
from clients.models import Client

#ctx es el diccionario vacio creado en pv.py
#Decorador para que clients sea un grupo(otro decorador)
@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command() #Con esto ya es comando de clients 
#   CLASE41: 
#   Click ayuda a perdir al usuario crenado la opción
#   Shortname -n y Longname --name
@click.option('-n','--name',
              type=str,
              prompt=True,
              help='The client name')
@click.option('-c','--company',
              type=str,
              prompt=True,
              help='The client company')
@click.option('-e','--email',
              type=str,
              prompt=True,
              help='The client email')
@click.option('-p','--position',
              type=str,
              prompt=True,
              help='The client position')
@click.pass_context #Pasar el contexto
def create(ctx, name, company, email, position):
    """Creates a new client"""
    #  CLASE 41:
    #  Se crea el cliente y el servicio y finalmente
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])
    #  Se usa la función create_client del archivo service.py
    client_service.create_client(client)
    

@clients.command() #Con esto ya es comando de clients 
@click.pass_context #Pasar el contexto
def list(ctx):
    """List all clients"""
    #  CLASE 42:
    #  Referencia al ClientService, inicializando la clase
    client_service = ClientService(ctx.obj['clients_table'])
    #  Se usa la función list_client del archivo service.py
    clients_list = client_service.list_clients()
    # Usamos click.echo (Consola) a cambio de print
    click.echo ('ID  |  NAME  |  COMPANY  |  EMAIL  |  POSITION')
    click.echo ('*'*100)
    #   Iteración para los clientes
    for client in clients_list:
        click.echo('{uid}  |  {name} | {company}   | {email} | {position}'.format(
            uid=client['uid'],
            name=client['name'],
            company=client['company'],
            email =client['email'],
            position =client['position']))


@clients.command() #Con esto ya es comando de clients 
#   CLASE44
@click.argument('client_uid',
                type=str)
@click.pass_context #Pasar el contexto
def update(ctx, client_uid):
    """Update a client"""
    #   CLASE 44:
    #   Referencia al ClientService, inicializando la clase
    client_service = ClientService(ctx.obj['clients_table'])
    #  Se usa la función list_client del archivo service.py
    client_list = client_service.list_clients()
    # List comprehension para ubicar el row del cliente
    client = [client for client in client_list if client['uid'] == client_uid]
    # Condicional para hacer actualización
    if client:
        # Envia a un nuevo metodo _update_client_flow
        #  Se usa la función update del archivo service.py
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)
        click.echo ('Client update')        
    else:
        click.echo ('Client not found')


def _update_client_flow(client):
    click.echo ('Leave empty if you dont want to modify the value')    
    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)

    
@clients.command() #Con esto ya es comando de clients 
@click.pass_context #Pasar el contexto  
def delete(ctx, client_uid):
    """Delete a client"""
    pass

all = clients
