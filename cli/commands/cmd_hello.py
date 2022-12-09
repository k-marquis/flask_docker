import os
import subprocess

import click

@click.command
@click.argument('name', default='Kris')
def cli(name):
    """
    Run tests with Pytext

    Args:
        path: Test coverage path.
    Return:
        subprocess call result
    """
    
    msg = f'Hi {name}!'
    return print(msg)