import click
from clients import commands as clients_commands 
"""Importando los comandos asignando nuevo nombre"""

CLIENT_TABLE = 'clients.csv'

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['clients_table'] = CLIENT_TABLE
#ctx se inicia como diccionario vacio

"""Registrando todos los comandos"""
cli.add_command(clients_commands.all)