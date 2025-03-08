import click

# 通过装饰器click.command() 声明一个命令的执行操作
# click.option 定义一个命令的选项 --count 默认为1 help --help执行说明
# click.argument 定义命令的参数
# ex: python command.py --count 2 test
# output: 
#          Hello test
#          Hello test
@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo(f'Hello {name}')

if __name__ == '__main__':
    hello()
