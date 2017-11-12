#encoding:utf-8
import unittest
from history import RunMain

class TestMethod(unittest.TestCase):
    #每次类执行之前执行
    @classmethod
    def setUpClass(cls):
        print '类执行之前的方法'
        
    #每次类执行之后执行
    @classmethod
    def tearDownClass(cls):
        print '类执行之后的方法'
    
    #每次方法之前执行
    def setUp(self):
        print 'test--->setup'
        
    #每次方法后执行
    def tearDown(self):
        print 'test---->teardown'
        
    def test_01(self):
        print '这是一个测试方法'
        
    def test_02(self):
        print '这是第二个测试方法'
        
if __name__=='__main__':
    unittest.main()