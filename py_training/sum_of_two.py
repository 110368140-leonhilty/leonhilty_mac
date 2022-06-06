def sum_of_two(data, k):
    for a_index,a_value in enumerate(data):
        for b_index,b_value in enumerate(data):
            if a_index != b_index and a_value + b_value==k:
                return [a_index, b_index]
    return []
print(sum_of_two([1,2,3,4,5,6,7,11,15],26))
print('-'*50)
#-----------------
from itertools import combinations

for c in combinations([1,2,3,4,5],2):
    print(c)
print('-'*50)
def two_sum(data,k):

    for a,b in combinations(enumerate(data),2):
        if a[1]+ b[1] == k :
            return [a[0],b[0]]
    return []

print(two_sum([1,2,3,4,5],8))

