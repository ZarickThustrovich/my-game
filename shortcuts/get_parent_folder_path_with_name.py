import os


def get_parent_folder_path_with_name(name):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), f'sprites/{name}')
