import click

from core.vars.http import http
from default.router.NameFactory import name_extend
from tamp.interface.order import OrderAbs


@click.command('routes')
def routes():

    for route in http.query_router():

        click.echo(route)


orders = [routes]


class Plan0RouterOrder(OrderAbs):
    name = name_extend

    def get_orders(self) -> list:

        return orders
