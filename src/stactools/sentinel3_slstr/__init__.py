import stactools.core
from stactools.sentinel3_slstr.stac import create_item

__all__ = ["create_item"]

stactools.core.use_fsspec()


def register_plugin(registry):
    from stactools.sentinel3_slstr import commands

    registry.register_subcommand(commands.create_sentinel3slstr_command)


__version__ = "0.1.0"
