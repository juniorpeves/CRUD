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
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])
    
    client_service.create_client(client)
    

@clients.command() #Con esto ya es comando de clients 
@click.pass_context #Pasar el contexto
def list(ctx):
    """List all clients"""
    pass


@clients.command() #Con esto ya es comando de clients 
@click.pass_context #Pasar el contexto
def update(ctx, client_uid):
    """Update a client"""
    pass


@clients.command() #Con esto ya es comando de clients 
@click.pass_context #Pasar el contexto  
def delete(ctx, client_uid):
    """Delete a client"""
    pass

all = clients
