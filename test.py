# coding:utf-8
person_message = {"name":'zhaojianxing',"age":26,"height":"171cm","weight":"62.5kg"}

school_message = {"s_name":'华北科技学院','s_address':'燕郊'}
"""
这是一种合并字典的方法，很是方便简洁
"""

dict1 = dict(person_message,**school_message)

print(dict1)
 

