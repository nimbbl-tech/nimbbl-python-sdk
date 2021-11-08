import nimbbl
import os
import unittest
import json

def mock_file(filename):
    if not filename:
        return ''
    file_dir = os.path.dirname(__file__)
    file_path = "{}/mocks/{}.json".format(file_dir, filename)
    with open(file_path) as f:
        mock_file_data = json.load(f)
    return mock_file_data


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        access_key="access_key_81x7ByYkREmW205N"
        secret_key="access_secret_ArL0OKDKBGx5A0zP"
        self.base_url = 'https://uatapi.nimbbl.tech/api'
        self.client = nimbbl.Client(access_key,secret_key)
