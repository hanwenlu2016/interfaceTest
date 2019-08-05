import requests
from common.Log import logger


# 重新封装  requests
class RunMain():

    def send_post(self, url, data, headers):
        if headers != '':
            result = requests.post(url=url, headers=headers, data=data)
            return result
        else:
            result = requests.post(url=url,  data=data)
            return result

    def send_get(self, url, data, headers):

        if headers != '':
            result = requests.post(url=url, headers=headers, data=data)
            return result
        else:
            result = requests.post(url=url, data=data)
            return result

    def run_main(self, method, url=None, data=None, headers=None):
        result = None

        if method == 'post':
            result = self.send_post(url=url, headers=headers, data=data)

        elif method == 'get':
            result = self.send_get(url=url, headers=headers, data=data)

        else:

            logger.info("method值错误！！！")

        return result
