import requests


class IhrmLoginApi:
    @classmethod
    def login(cls, data_json):
        resp = requests.post(url="https://ihrm-java.itheima.net/api/sys/login",
                             json=data_json)
        return resp