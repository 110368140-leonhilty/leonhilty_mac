import statistics #統計資料用
def find_majority_num(data):
    return statistics.mode(data) #mode 眾數


print(find_majority_num([1,2,2,2,3,4,4,5,5,5,5]))
