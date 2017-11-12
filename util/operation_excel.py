#incoding:utf-8
import xlrd
"""
data=xlrd.open_workbook('')
tables=data.sheets()[0] #获取sheet
print tables.nrows #获取行数
print tables.cell_value(2,3) #获取第2行第3列的值
"""
class OperationExcel:
    
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name=file_name
            self.sheet_id=sheet_id
        else:
            self.file_name='文件路径'
            self.sheet_id=0
        self.data=self.get_data()
     
     #获取表   
    def get_data(self):
        data=xlrd.open_workbook(self.file_name)
        tables=data.sheets()[self.sheet_id]
        return tables
    
    #获取行数
    def get_lines(self):
        tables=self.data()
        return tables.nrows
    
    #获取单元格
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)
    
if __name__=='__main__':
    opers=OperationExcel()
    print opers.get_data(file_name, sheet_id).nrows
