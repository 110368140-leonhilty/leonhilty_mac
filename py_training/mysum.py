def mysum(*word):
    if not word:
        return word
    output = word[0]
    for i in word[1:]:
        output += i
    return output

print(mysum())
print(mysum(10,20,30,40)) #INT
print(mysum('a','v','w')) #String
print(mysum([10,20,30],[40,50],[60])) #LIST