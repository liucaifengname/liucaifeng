import HTMLTestRunner
import os
import unittest
import time


report_path=os.path.dirname(os.path.abspath('.'))+'./test_report/'
now=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))

HtmlFile=report_path + now + '_result.html'


fp=open(HtmlFile,'wb')

suite=unittest.TestLoader().discover('testsuites',pattern='test*.py')

if __name__ == '__main__':

    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='WEB UI 自动化测试报告，测试结果如下',)
    runner.run(suite)
    fp.close()