import click
from clients import commands as clients_commands 
"""Importando los comandos asignando nuevo nombre"""

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
#ctx se inicia como diccionario vacio

"""Registrando todos los comandos"""
cli.add_command(clients_commands.all)