import click
from core.proj.abs import ProjectAbs
from core.order.unity import orders


@click.group()
def executor():
    click.echo("\n")
    click.echo("                            _ooOoo_  ")
    click.echo("                           o8888888o  ")
    click.echo("                           88  .  88  ")
    click.echo("                          (| - _ - |)  ")
    click.echo("                           O\\  =  /O  ")
    click.echo("                        ____/`---'\\____  ")
    click.echo("                      .   ' \\| |// `.  ")
    click.echo("                       / \\||| : |||// \\  ")
    click.echo("                     / _||||| -:- |||||- \\  ")
    click.echo("                       | | \\\\\\ - /// | |  ")
    click.echo("                     | \\_| ''\\---/'' | |  ")
    click.echo("                      \\ .-\\__ `-` ___/-. /  ")
    click.echo("                   ___`. .' /--.--\\ `. . __  ")
    click.echo("                ."" '< `.___\\_<|>_/___.' >'"".  ")
    click.echo("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |  ")
    click.echo("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /  ")
    click.echo("         =======`-.____`-.___\\_____/___.-`____.-'=======  ")
    click.echo("                            `=------='  ")
    click.echo("  ")
    click.echo("         .............................................  ")
    click.echo("                佛祖镇楼                  BUG消失  ")


def unity_order_loader(e):
    for order in orders:
        e.add_command(order)


def extends_order_loader(e, project: ProjectAbs):
    extends = project.extends

    commands = []
    for name in extends.query_names_order():
        commands.extend(extends.query_order(name).get_orders)

    for command in commands:
        e.add_command(command)


def loader(project: ProjectAbs):
    e = executor
    unity_order_loader(e)
    extends_order_loader(e, project)

    return e
