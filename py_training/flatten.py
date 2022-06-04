#把二維陣列壓平為一為陣列 [[1,2],[3,4]] -> [1,2,3,4]


# def flatten(data_list):
#     output = []
#     for array in data_list:
#         for elemnet in array:
#             output.append(elemnet)
#     return output

#使用生成式

def flatten(data):
    return [sub_element
     for elemnet in data
     for sub_element in elemnet]



print(flatten([[1,2],[3,4]]))