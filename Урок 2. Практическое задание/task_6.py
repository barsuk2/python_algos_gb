"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import random
x = int(random.randint(0, 100))
print(x)

def rand (total =5):
    num = int(input().rstrip())
    if total == 1:
        print('Попытки закончены')
        return
    if num > x:
        print(f'Ваше число больше X, осталось попыток {total-1}' )
        rand(total-1)
    elif num < x:
        # total -= total
        print(f'Ваше число меньше X, осталось попыток {total-1}')
        rand(total-1)
    else:
        print('Вы угадали')


rand()