"""CLI entrypoint 'notebook' command"""

import click


@click.group()
@click.pass_context
def notebook(ctx, **kwargs):
    """CLI entrypoint and base command"""

    ctx.ensure_object(dict)
    ctx.obj.update(kwargs)
