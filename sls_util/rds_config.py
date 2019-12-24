import os


def test_connector():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return "Directory Path is : " + str(dir_path)
