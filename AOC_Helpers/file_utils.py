import ast


def list_from_file(file_path):
    """
    Read the file containing the brick data and parse it into a Python list.

    :param file_path: Path to the file containing the brick data.
    :return: Parsed list of bricks.
    """
    with open(file_path, 'r') as file:
        data = file.read()
        ls = ast.literal_eval(data)
    return ls