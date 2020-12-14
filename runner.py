

from util import HTMLTestReportCN,createLogging
import unittest
import time
import logging
from config.configs import casefile,list_go,test_user,project_name



#添加casefile所有测试用例。
def createsuite():
    logging.info('开始添加用例')
    testunit = unittest.TestSuite()
    for x in list_go:
        discover = unittest.defaultTestLoader.discover(casefile,pattern=x,top_level_dir=None)
        for test_suite in discover:
            for test_case in test_suite:
                testunit.addTests(test_case)
        logging.info(str(x)+'下的用例添加成功')
    return testunit

#控制台输出启动
createLogging.createLogger()
now = time.strftime("%Y-%m-%d_%H_%M_%S")
#测试报告存放的位置
filepath = 'report/AceReport_' + now +'.html'
fp = open(filepath,'wb')
runner = HTMLTestReportCN.HTMLTestRunner(
    stream=fp,
    title=project_name,
    tester=test_user
)
case = createsuite()
logging.info('自动化用例执行中...请稍等...\n用例进度：')
runner.run(case)
logging.info('Done')
fp.close()