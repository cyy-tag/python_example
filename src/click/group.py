import click
# 命令和组 通过command 和 Group实现

# 使用click.group 定义一个命令组 cli
# 并且接收一个参数 debug
@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo(f'Debug mode is {debug}')

# 用cli组 command修饰一个命令
# 当任何一个子命令被调用的时候，都会优先调用命令组cli再调用子命令
# python group.py --debug sync
@cli.command()
def sync():
    click.echo('Syncing')

if __name__ == '__main__':
    cli()

