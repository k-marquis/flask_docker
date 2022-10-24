import subprocess

import click

@click.command()
@click.option('--skip-init/--no-skip-init',default=True,
               help='Skip __init__.py files?')
@click.argument('path', default='pomoapp')
def cli(skip_init,path):
    """
    Run flake8 to analyze your code base

    Args:
        skip_init: Skip checking  __init__.py files.
        path: Test coverage path
    Return:
        Subprocess call result
    """
    flake8_flag_exclude = ''
    
    if skip_init:
        flake_flag_exclude = ' --exclude __init__.py'
    
    cmd = f'flake8 {path}{flake_flag_exclude}'
    return subprocess.call(cms, shell=True)
