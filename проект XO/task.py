# размер в клетках для игрового поля
board_size = 3
# игровое поле
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def draw_board():
    '''
    Вывод игрового поля
    :return:
    '''

    print(('_' * 4 * board_size))

    for i in range(board_size):
        print((' ' * 3 + '|') * 3)
        print('', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print(('_' * 3 + '|') * 3)


def check_win():
    '''
    Проверка на победу одного из игроков
    :return:
    '''
    win = False

    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонталь
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикаль
        (0, 4, 8), (2, 4, 6)  # диагональ
    )

    for pos in win_combination:
        # если три ячейки совпадает

        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]] and board[pos[1]] in ('X', 'O')):
            win = board[pos[0]]

    return win


def game_step(index, char):
    '''
    Функция хода игрока
    :param index:
    :param char:
    :return:
    '''

    if (index > 10 or index < 1 or board[index - 1] in ('X', 'O')):
        return False

    board[index - 1] = char
    return True


def start_game():
    # текущий игрок
    current_player = 'X'
    # номер шага
    step = 1

    draw_board()

    # игра продолжается до тех пор, пока кто-то не выиграет или выйдет
    while (step < 10) and (check_win() == False):
        index = input('Ходит ' + current_player + '. Введите номер поля (0 - выход):')

        if (int(index) == 0):
            break

        # если получилось сделать шаг
        if (game_step(int(index), current_player)):
            print('Удачный ход')

            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'

            draw_board()
            # увеличим номер шага
            step += 1
        else:
            print('Неверный номер! Повторите!')

    if (step == 10):
        print('Игра закончена. Ничья!')
    else:
        print('Выиграл ' + check_win() + 'Игра закончена')


print('Добро пожаловать в игру Крестики - Нолики!')
start_game()
