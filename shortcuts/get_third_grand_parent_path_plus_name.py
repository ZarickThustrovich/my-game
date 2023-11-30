import os
from .get_third_grand_parent import get_third_grand_parent


def get_third_grand_parent_path_plus_name(file, name):
    return os.path.join(
        get_third_grand_parent(file),
        name,
    )
