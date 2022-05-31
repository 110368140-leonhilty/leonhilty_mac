import operator #可以取代 lambda 主要指定list or tuple 排序

d = [1,3,4,5,6,7]

select = operator.itemgetter(1)

select2 = operator.itemgetter(4,2)

print(select(d))
print('-'*50)
print(select2(d))