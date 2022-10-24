import os
import subprocess

import click

@click.command
@click.argument('path', default=os.path.join('pomoapp','tests'))
def cli(path):
    """
    Run tests with Pytext

    Args:
        path: Test coverage path.
    Return:
        subprocess call result
    """
    
    cmd = 'py.test {0}'.format(path)
    return subprocess.call(cmd, shell=True)