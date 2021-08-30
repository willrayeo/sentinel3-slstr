import os
import sys

from stac import create_item


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

    return item


if __name__ == "__main__":

#     input_file = "/home/mlamare/Downloads/S1A_IW_GRDH_1SDV_20210809T173953_20210809T174018_039156_049F13_6FF8.SAFE"
    input_file = "/Users/williamray/Repositories/sentinel3-slstr/tests/data-files/S3A_OL_1_EFR____20210827T074336_20210827T074636_20210828T115721_0179_075_320_3060_LN1_O_NT_002.SEN3"
    # input_file = "/home/mlamare/Downloads/S1B_EW_GRDM_1SDH_20210813T063842_20210813T063942_028224_035DEE_6523.SAFE"
    output_dir = "/Users/williamray/Repositories/sentinel3-slstr/tests/output"

    item = create_item_command(input_file, output_dir)

    print(item)
