import HTMLTestRunner
import os
import unittest
import time

test_dir = './'
suite=unittest.TestLoader().discover(test_dir,pattern='test*.py')
report_path=os.path.dirname(os.path.abspath('.'))+'./test_report/'
HtmlFile=report_path  + '_result.html'
fp=open(HtmlFile,'wb')

if __name__ == '__main__':

    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'WEB UI 自动化测试报告，测试结果如下',description=u"用例测试情况如下")
    runner.run(suite)
    fp.close()




