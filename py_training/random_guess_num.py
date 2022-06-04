import random

def guessing_game():
    answer = random.randint(0,99)
    while True:
        guess_num = (input('請輸入0~99數字：'))
        if guess_num.isdigit():
            guess_num = int(guess_num)
        if guess_num == answer:
            print('你猜中了')
            break
        elif guess_num > answer:
            print('你猜太高了')
        else:
            print('你猜太低了')

guessing_game()