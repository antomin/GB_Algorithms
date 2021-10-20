"""
В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, то вывести загаданное число.
"""

from random import randint

sec_num = randint(0, 100)
attempts = 10
cnt = 1
while cnt <= attempts:
    user_answer = int(input('Enter your number: '))
    if int(user_answer) == sec_num:
        print(f'YOU WIN!!!\n{user_answer} is correct answer.')
        break
    elif user_answer < sec_num:
        print(f'NO.\nMy number is more than {user_answer}.')
    else:
        print(f'NO.\nMy number is less than {user_answer}.')
    print(f'You have {attempts - cnt} more attempts')
    cnt += 1
else:
    print(f'GAME OVER(\nCorrect answer is {sec_num}.')
