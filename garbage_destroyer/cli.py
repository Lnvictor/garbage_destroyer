#!/usr/bin/env python
import click
from clean import clean


@click.group()
def garbage_destroyer_cli():
    click.echo(click.style("Exectuing Garbage destroyer...", fg='cyan'))


@click.command()
@click.option('--ext', default='', help='Filter for delete only a specified file extension')
@click.argument('time_diff')
@click.argument('dir')
def execute_on_time(ext, time_diff, dir):
    click.echo(click.style("Exectuing cleaning on the time", fg='cyan'))
    clean(time_diff=int(time_diff), ext=ext, dir=dir)
    click.echo(click.style("Finished.", fg='green'))


garbage_destroyer_cli.add_command(execute_on_time)


if __name__ == '__main__':
    garbage_destroyer_cli()