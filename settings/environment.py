from .app import RESOLUTION
from shortcuts import get_parent_folder_path_with_name


ENVIRONMENT_SPRITES_FOLDER = get_parent_folder_path_with_name('tiles')
SURFACE_BOTTOM_BORDER=RESOLUTION[1] - 100
TILE_DEFAULT_SIZE = [50, 50]