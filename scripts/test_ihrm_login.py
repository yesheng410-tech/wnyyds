import unittest


from parameterized import parameterized

from api.ihrm_login_api import IhrmLoginApi
from common.assert_util import common_assert
from common.read_json_data import read_json


class TestIhrmLogin(unittest.TestCase):
    @parameterized.expand(read_json())
    def test_ihrm_login(self, desc, req_data, status_code, success, code, message):
        resp = IhrmLoginApi.login(req_data)
        print(f'{desc}:{resp.json()}')

        common_assert(self, resp, status_code, success, code, message)
