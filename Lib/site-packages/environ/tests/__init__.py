import os

TESTS_DATA_PATH = os.path.dirname(__file__)


def get_test_data_filepath(file):
    return os.path.join(TESTS_DATA_PATH, file)