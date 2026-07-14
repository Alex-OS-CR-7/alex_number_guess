""" Числовая Угадайка 
    Мини-проект из курса
    'Поколение Python'
"""
import random as r

print(
    'Добро пожаловать в числовую угадайку!',
    'Правила весьма просты!',
    'Вы должны угадать число, которое я загадал.',
    'Самое малое число будет равно "1"',
    'Самое большое число выбираете Вы!',
    sep='\n'
    )

max_border = int(input('Введите правую границу угадайки (например: 100):'))

programm_random_num = r.randint(1,max_border)



def is_valid_num(user_num_input):
    if user_num_input.isdigit():
        if int(user_num_input) >= 1 and int(user_num_input) <= max_border:
            return True
    else:
        return False 

curcle_input_flag = True
user_try_counter = 0

while curcle_input_flag == True:
    user_num_input = input(f"Введите число от 1 до {max_border}:")
    user_try_counter += 1
    if is_valid_num(user_num_input) == True:
        n = int(user_num_input)
        if n == programm_random_num:
            print(
                'Вы угадали, поздравляем!'
            )
            print(
                'Хотите сыграть еще?',
                'Если да, введите "1"',
                'Если нет, ввдетие "0"',
                sep='\n'
                )
            user_answer = int(input('Введите 1 или 0:'))
            if user_answer == 1:
                print('Начинаем сначала!')
                max_border = int(input('Введите правую границу угадайки (например: 100):'))
                programm_random_num = r.randint(1,max_border)
                continue
            else:
                print(
                'Спасибо, что играли в числовую угадайку.',
                'Еще увидимся...',
                sep='\n'
            )
            curcle_input_flag = False
        elif n < programm_random_num:
            print('Ваше числе меньше загаднного, попробуйте еще разок!')
        elif n > programm_random_num:
            print('Ваше число больше загаданного, попробуйте еще разок!')
    elif is_valid_num(user_num_input) == False:
        print('А может быть все-таки введем целое число?')
        continue
