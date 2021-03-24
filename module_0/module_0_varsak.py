import numpy as np


def game_core(number):
    '''Устанавливаем любое число, а затем сокращаем диапазон искомых значений 
    в зависимости от того, больше или меньше оно середины диапазона'''

    range_min = 1  # начало диапазона
    range_max = 100  # конец диапазона
    range_middle = (range_min+range_max) // 2  # середина диапазона

    # загадываем число в диапазоне
    predict = np.random.randint(range_min, range_max+1)
    tries = 1  # счетчик числа попыток

    while predict != range_middle:
        tries += 1  # засчитываем попытку
        # Проверяем, больше или меньше число середины диапазона
        if predict > range_middle:
            #сужаем диапазон к максимальной границе
            range_min = range_middle + 1
        else:
            #сужаем диапазон к минимальной границе
            range_max = range_middle - 1
   
        # Формируем новое значение середины диапазона
        range_middle = (range_min + range_max) // 2
    return(tries)  # выход из цикла, если число угадано


def score_game(game_core):  # функция для тестирования из задания
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксир RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core)  # тестируем
