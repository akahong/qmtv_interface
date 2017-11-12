#incoding:utf-8

class globle_var:
    #case_id
    Id='0'
    url='1'
    run='2'
    request_way='3'
    header='4'
    case_depend='5'
    data_depend='6'
    field_depend='7'
    data='8'
    expect='9'
    result='10'
    
#获取caseid
def get_id():
    return globals.Id

#获取接口地址
def get_url():
    return globals.url

#获取是否执行信息
def get_run():
    return globals.run

#获取请求方式
def get_request_way():
    return globals.request_way

#获取header
def get_header():
    return globals.header

#获取依赖id
def get_case_denpend():
    return globals.case_depend

#获取依赖数据
def get_data_depend():
    return globals.data_depend

#获取依赖数据所属字段
def get_field_depend():
    return globals.field_depend

#获取数据
def get_data():
    return globals.data

#获取预期结果
def get_expect():
    return globals.expect

#获取实际结果
def get_result():
    return globals.result

#获取header的值
def get_header_value():
    header={
    "header":"1234",
    "cookie":"aka"
    }

    