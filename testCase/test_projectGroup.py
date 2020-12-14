
import sys,json
import requests

from util.screenShot import screenshot
from util.caseTemplate import Template


#测试用例
class MyTestCase_projectgroup(Template):
    def testCase_getlist(self):
        url = 'https://ace-test.altstory.com/project_group/list'
        data = {
        "filter":{"name":""},
        "pagination":{"page":1,"limit":16}
        }
        url_web = 'https://ace-test.altstory.com/home'
        screenshot(url_web,'MyTestCase_projectgroup_testCase_getlist',self.driver)
        r = requests.post(url=url,headers=self.headers,data=json.dumps(data))
        sys.stdout.write("\n请求url:"+str(url)+"\n请求参数:"+str(data)+'\n')
        self.assertEqual(r.status_code,200, "testError")
        self.assertIn('data',r.json().keys())



