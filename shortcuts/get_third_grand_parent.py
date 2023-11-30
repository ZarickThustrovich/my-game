import os


def get_third_grand_parent(file):
    return os.path.dirname(
            os.path.dirname(
                os.path.dirname(file)
                )
            )
