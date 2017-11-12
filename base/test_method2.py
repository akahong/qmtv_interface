#incoding:utf-8
import unittest
import json
from history import RunMain
import HTMLTestRunner
import mock
from mock_demo import mock_test

class TestMethod(unittest.TestCase):
    
    def setUp(self):
        self.run=RunMain()
        
    def test_01(self):
        #背包
        url='https://www.quanmin.tv/shouyin_api/user/rich/payment_reward_config?'
        'debug=1&cid=6&conn=WWAN&cv=iphone2_3.4.40&debug=0&dev=595A3548-ED04-4672-B5DE-9D34A22D6311&'
        'nonce=ZDZELOIBQSUPYLZIVOBTWNJGHAMSJGQO&os=30&osversion=ios_10.2.1&'
        'sid=e3b09f74ade6ac5f90cdb223e665e0a9&sign=F81513E2D8BEAB667EDF7D2B91711F15&'
        'toid=2094966074&token=v9fvSY9a8aab6b&ua=iPhone6%2C1'
        res=mock_test(self.run.run_main,url,'GET','18976729870')
        """
        mock_data=mock.Mock(return_value=18976729870)
        print mock_data
        self.run.run_main=mock_data
        res=self.run.run_main(url, 'GET',data=None)
        
        """
        print res
        print '第一个case'
   # @unittest.skip('test_02')    
    def test_02(self):
        
        #牛币数
        url='https://api-shouyin.quanmin.tv/user/rich/get?'
        'cid=6&conn=3G&cv=iphone2_3.4.40&debug=0&dev=595A3548-ED04-4672-B5DE-9D34A22D6311'
        '&nonce=YMDWWNXTGYPZTQSBECVCSIPBYIWQBOYS&osversion=ios_10.2.1&sid=e3b09f74ade6ac5f90cdb223e665e0a9'
        '&sign=4FD93F79642BB11974F50FA13BA54A89&toid=2094966074&token=v9fvSY9a8aab6b&ua=iPhone6%2C1'
        res=self.run.run_main(url,'GET',data=None)
        print res
        print '第二个case'
    def tearDown(self):
        pass
if __name__=='__main__':
    """
    filepath="/Users/feidong/base/report.html"
    fp=file(filepath,'wb')
    suit=unittest.TestSuite()
    suit.addTest(TestMethod('test_02'))
    suit.addTest(TestMethod('test_01'))
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is report')
    runner.run(suit)
    """
    suit=unittest.TestSuite()
    suit.addTest(TestMethod('test_02'))
    suit.addTest(TestMethod('test_01'))
    unittest.TextTestRunner().run(suit)
    