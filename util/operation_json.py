#incoding:utf-8
import json

"""
fp=open('文件路径')#加载文件路径
data=json.load(fp) 
print data['键值']
"""

class OperatinJson:
    
    def __init__(self):
        self.data=self.read_data()
        
    #读取json文件
    def read_data(self):
        with open('文件路径') as fp:
            data=json.load(fp)
            return data
    
    #根据关键字获取数据
    def get_data(self,id):
        return self.data[id]
    
if __name__=='__main__':
    opjson=OperatinJson()
    print opjson.get_data(id)
        
    