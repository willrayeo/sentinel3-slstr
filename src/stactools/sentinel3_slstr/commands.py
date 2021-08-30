import click
import logging
import os

from stactools.sentinel3_slstr.stac import create_item

logger = logging.getLogger(__name__)


def create_sentinel3slstr_command(cli):
    """Creates the stactools- command line utility."""
    @cli.group(
        "sentinel3slstr",
        short_help=("Commands for working with stactools-"),
    )
    def sentinel3slstr():
        pass

    @sentinel3slstr.command(
        "create-item",
        short_help="Convert a Sentinel3 SLSTR scene into a STAC item",
    )
    @click.argument("src")
    @click.argument("dst")
    def create_item_command(src, dst):
        """Creates a STAC Collection

        Args:
            src (str): path to the scene
            dst (str): path to the STAC Item JSON file that will be created
        """
        item = create_item(src)

        item_path = os.path.join(dst, "{}.json".format(item.id))
        item.set_self_href(item_path)

        item.save_object()

        return sentinel3slstr
