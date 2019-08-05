import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import readExcel
import json
from common.Log import logger

log = logger
url = geturlParams.geturlParams().get_Url()  # 调用我们的geturlParams获取我们拼接的URL
login_xls = readExcel.readExcel().get_xls('1.xlsx', 'login') #读取测试用列


@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):

    def setParameters(self, case_name, path, query, header, method, result):
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
        self.header = eval(header)
        self.result = result

    def description(self):
        self.case_name

    def setUp(self):
        print(self.case_name + "测试开始前准备")
        log.info(self.case_name + "测试开始前准备")
    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")
        log.info(self.case_name + "测试结束！")

    def checkResult(self):  # 断言

        new_url = url + self.path
        info = RunMain().run_main(self.method, url=new_url, headers=self.header, data=self.query)
        code = info.json()
        if self.case_name == 'login1':
            self.assertEqual(info.status_code, 200)
            self.assertEqual(json.dumps(code), self.result)
            print('请求结果: {}'.format(code))
            log.info('请求结果: {}'.format(code))
        if self.case_name == 'login2':
            self.assertEqual(info.status_code, 200)
            print('请求结果: {}'.format(code))
            log.info('请求结果: {}'.format(code))


if __name__ == "__main__":
    unittest.main(verbosity=1)

# '''
# verbosity
# 0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共100个 失败20 成功80
# 1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
# 2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
# '''
