import click

# 嵌套处理和上下文传递
# pass_context装饰器标记自己来请求传递上下文
# 在这种情况下, 上下文作为第一个参数传递
@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    ctx.obj['DEBUG'] = debug # 修改上下文

# 使用click.pass_context 修饰接收上下文
@cli.command()
@click.pass_context
def sync(ctx):
    click.echo('Debug is %s' % (ctx.obj['DEBUG'] and 'on' or 'off'))

if __name__ == '__main__':
    cli(obj={})
