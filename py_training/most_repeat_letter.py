from collections import Counter 
import operator

def most_repeated_letter(word):
    letters = list(set(word))
    letters_count = []
    for letter in letters:
        letters_count.append((letter,word.count(letter)))
    
    result = sorted(letters_count,key=operator.itemgetter(1))[-1]
    print(f'{result[0]}重複了{result[1]}')
    

def most_repeated_letter2(word):
    result = Counter(word).most_common(1)[0]
    print(f'{result[0]}重複了{result[1]}')

most_repeated_letter('independence')
most_repeated_letter2('happy new_word')
#---------------------


s = 'banana'
letter = Counter(s)
print(letter)
print(letter.most_common(1)) #只回傳最多次數的letter 一個
