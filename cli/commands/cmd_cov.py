import subprocess
import click

@click.command
@click.argument('path', default="pomoapp")
def cli(path):
    """
    Run a test coverage report.

    Args:
        path: Test coverage path.
    Return:
        subprocess call result
    """
    
    cmd = 'py.test --cov-report term-missing --cov {0}'.format(path)
    return subprocess.call(cmd, shell=True)