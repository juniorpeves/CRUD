from setuptools import setup
"""Importar el modulo setup"""

setup(
    name='pv',
    version='0.1',
    py_modules=['pv'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pv=pv:cli
    ''',
)
# Nombre de la aplicacion pv
# Versiones la 0.1
# El modulo se llamada pv
# Requisito el modulo click
# El punto de entrada es el metodo cli (Declarado en pv.py)