#將 dict 的key and value 顛倒

#使用 生成式 {運算式,運算式 for 鍵,值 in 容器}


# def flipped_dict(dict_data):
#     return {value:key for key,value in dict_data.items()}

#只抓 key
def flipped_dict(dict_data):
    return {dict_data[key]:key for key in dict_data}




print(flipped_dict({'a':1,'b':2,'c':3}))
