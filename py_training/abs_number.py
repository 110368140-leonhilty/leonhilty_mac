#生成式 
# def abs_numbers(numbers):
#     return [abs(number) for number in numbers]


def abs_numbers(numbers):
    return list(map(abs,numbers))
#map(函式,容器)

print(abs_numbers([-1,-2,-3,5]))
