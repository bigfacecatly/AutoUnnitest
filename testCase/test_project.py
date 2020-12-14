

import sys,json
import requests
import configparser
from util.readConfig import ReadConfig_1,ReadConfig
from util.screenShot import screenshot
from util.caseTemplate import Template


config = configparser.ConfigParser()
#读取配置环境参数
config.read(ReadConfig())
# config.read(ReadConfig_1()+"project.ini")


#测试用例
class MyTestCase_project(Template):
    # 填写所需参数
    project_group_id = config['MyTestCase_group']['project_group_id']
    # data = config['MyTestCase_group']['data']
    #获取章节列表页
    def testCase_list(self):
        #配置参数
        self.headers['project_group_id'] = self.project_group_id
        #填写接口的url与请求参数
        url = 'https://ace-test.altstory.com/project/list'
        data = {
            "filter": {"project_group_id": int(self.project_group_id), "project_name": ""}
        }
        r = requests.post(url=url,headers=self.headers,data=json.dumps(data))
        #请求参数编写
        sys.stdout.write("\n请求url:"+str(url)+"\n请求参数:"+str(data)+'\n')

        # 对应的web页面截图地址
        url_web = 'https://ace-test.altstory.com/group/list?groupId=%s' % self.project_group_id
        screenshot(url_web, 'MyTestCase_project_testCase_list', self.driver)
        #断言
        self.assertEqual(r.status_code,200, "testError")
        self.assertIn('project_group_id',r.json()['data']['result'][0].keys())






