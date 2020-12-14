

需要python3 与pip3


安装虚拟环境
pip3 install pipenv

安装包
pipenv install 

启动命令 
python3 runner.py


查看结果报告

将report下 的html 报告 以网页形式打开即可


报告命名方式

AceReport_年-月-日 时_秒_分.html

详情可参考地址：https://doc.altstory.com/pages/viewpage.action?pageId=80053097



进度条功能 需要 在第三方库 unnitest的suite.py文件
在第一行导入模块 增加代码如下：
from tqdm import tqdm

将 110行附近的  for index,test in enumerate(self):
替换为：

list_case = []
for x in self:
	list_case.append(x)
for index in tqdm(range(len(list_case))):
	test= list_case[index]
