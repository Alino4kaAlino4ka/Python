import random

def take_candies(player:str, candies:int):
    max_candies = 28
    if candies < 28:
        max_candies = candies
    n_candies: int = 0
    while True:
        n_candies = int(input(f'игрок {player}, возьмите конфеты (от 1 до {max_candies}): '))
        if 0 < n_candies <= max_candies:
            break
    candies -= n_candies
    print(f'игрок {player} взял {n_candies} конфет')
    if candies == 0:
        print(f'игрок {player} победил!')
    return candies


def game_two_players():
    candies = 121
    print('Правила:\nНа столе лежит 2021 конфета.'
          ' Играют два игрока делая ход друг после друга.\n'
          ' Первый ход определяется жеребьёвкой.\n'
          ' За один ход можно забрать не более чем 28 конфет.')
    player_1 = input('Введите имя первого игрока: ')
    player_2 = input('Введите имя второго игрока: ')

    player = random.choice((player_1, player_2))
    print(f'Первым ходит игрок {player}')
    player_dict = {1: player}
    if player == player_1:
        player_dict[-1] = player_2
    else:
        player_dict[-1] = player_1
    # print(player_dict)
    # print(player_dict.get(1))
    count = 1
    while candies > 0:
        candies = take_candies(player, candies)
        print(f'на столе осталось {candies}')
        count *= -1
        player = player_dict.get(count)


def func():
    print('func from candy.py')
    print(__name__)


if __name__ == '__main__':
    user_choise = input('Выберите вариант 1 - два игрока, 2 - игра с ботом, q - для выхода: ')
    if user_choise == '1':
        game_two_players()
    # elif user_choise == '2':
    #     game_with_bot()
    elif user_choise == 'q':
        exit()
