import requests
import json 

class RunMain:
    """
    def __init__(self,url,method,data):
        res=self.run_main(url,method,data)
     """   
    def send_get(self,url,data):
        res=requests.get(url,data,verify=False)
        print res
        #return json.dumps(res,indent=2,sort_keys=True)
    
    def send_post(self,url,data):
        print 'no data'
        
    def run_main(self,url,method,data=None):
        res=None
        if method=='GET':
            res=self.send_get(url,data)
        else:
            res=self.send_post(url,data)
        return res
    """
if __name__=='__main__':
    url='https://api-shouyin.quanmin.tv/user/getHisView'
    data={
        'cid':6,
        'conn':'WWAN',
        'cv':'iphone2_3.4.40',
        'debug':0,
        'dev':'595A3548-ED04-4672-B5DE-9D34A22D6311',
        'nonce':'IUDEIVILOLWLSXDWPDXVIZHJCZVEWEWM',
        'os':'30',
        'osversion':'ios_10.2.1',
        'page':1,
        'sid':'e3b09f74ade6ac5f90cdb223e665e0a9',
        'sign':'8224F8B009303B0B16CFEC346D6FC9A1',
        'toid':'2094966074',
        'token':'v9cqSY5ee2b6c7',
        'ua':'iPhone6%2C1'
    }
    run=RunMain(url,'GET',data)
    print run
"""