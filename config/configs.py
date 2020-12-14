
#用例执行目录
casefile = "./testCase/"

#具体用例匹配规则
#需要执行的测试py文件 放入到list_go里面 文件全名如test_projectgroup.py  注意后缀也不能少
list_go = ['test_*.py']
# list_go = ['test_project.py','test_projectGroup.py','test_resource.py']
# list_go = ['test_project.py']
#测试人员名称
test_user = '李岩'

#测试项目
project_name = "ACE 自动化测试报告"

#环境配置 test测试环境    online 线上环境
APP_ENV = "test"