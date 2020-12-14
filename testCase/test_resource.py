


import sys
import requests

from util.readConfig import ReadConfig
from util.screenShot import screenshot
from util.caseTemplate import Template
import configparser
config = configparser.ConfigParser()

#读取配置环境参数
config.read(ReadConfig())



class MyTestCase_projectResource(Template):
    # 填写所需参数
    project_group_id = config['MyTestCase_group']['project_group_id']
    project_id = config['MyTestCase_projectResource']['project_id']
    blong = config['MyTestCase_projectResource']['blong']

    #章节上传图片dog.jpg
    def testCase_upload(self):
        contentType = self.headers['Content-Type']
        self.headers['project_group_id'] = self.project_group_id
        self.headers['project_id'] = self.project_id
        self.headers['belong'] = self.blong
        url = ''
        files={'file': open('testCase/img/yellow_dog.jpg','rb')}
        del self.headers['Content-Type']
        r = requests.post(headers=self.headers,url=url,files=files)
        self.headers['Content-Type'] = contentType

        url_web = '' % (self.project_group_id,self.project_id)
        screenshot(url_web, 'MyTestCase_projectResource_testCase_upload', self.driver)

        sys.stdout.write("\n请求url:" + str(url) + "\n请求参数:" + str(files) + '\n')
        self.assertEqual(r.status_code, 200, "testError")
        self.assertIn('yellow_dog.jpg', r.json()['data']['results'].keys())

