import random
# for i in range(1,10):
#     for j in range(9,i,-1):
#         print(' ',end='')

#     for k in range(1,i+1):
#         print(i,end=' ')
#     print()
#--------------------------------
# print(random.sample(['22', '33', '44', '55', '66', '77', '88'], 4)) # ['44', '33', '22', '66']
#-------------------------------

str_dic = {
    'zaa' : 101,
    'hello': 97,
    'good' : 98
}


a = []
sort_list=sorted(str_dic.items(), key=lambda x:x[1],reverse=True)


for i in range(len(sort_list)):
    print(sort_list[i][0])

