
import sys

from util.screenShot import screenshot
from util.caseTemplate import Template


#测试用例
#demo1请求百度
class MyTestCase3(Template):
    def testCase2(self):
        url = "http://baidu.com"
        screenshot(url,'MyTestCase3_testCase2',self.driver)
        sys.stdout.write("请求url:"+url+"\n请求参数:无")
        self.assertEqual(2, 2, "testError")



