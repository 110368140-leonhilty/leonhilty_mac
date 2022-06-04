#利用生成式
# def sum_numbers(numbers):
#     return sum([int(number)
#     for number in numbers.split()
#     if  number.isdigit()])

#利用filter(函式,容器) 結果為True保留 用來過濾容器元素

def sum_numbers(number):
    return sum(list(
        map(int,
            filter(lambda d: d.isdigit(),number.split())))
    )



print(sum_numbers('11 11dd 24 dd'))
