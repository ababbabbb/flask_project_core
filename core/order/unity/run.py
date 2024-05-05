import click

from core.vars.application import application
from core.vars.info import info


@click.command('run')
def run():

    application.app.run(
        host=info.query('ip'),
        port=info.query('port'),
        *info.query('args'),
        **info.query('kwargs')
    )
