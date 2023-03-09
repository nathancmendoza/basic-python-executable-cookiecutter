"""
    :module_name: cli
    :module_summary: a CLI for {{cookiecutter.package_name}}
    :module_author: {{cookiecutter.package_author}}
"""

import click

@click.command()
def {{cookiecutter.project_name}}():
    """Entry point to {{cookiecutter.project_name}}"""
    click.echo('Hello World!')
