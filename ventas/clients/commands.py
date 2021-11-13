import click

#ctx es el diccionario vacio creado en pv.py
#Decorador para que clients sea un grupo(otro decorador)
@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command() #Con esto ya es comando de clients 
@click.pass_context #Pasar el contexto
def create(ctx, name, company, email, position):
    """Creates a ew client"""
    pass


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
