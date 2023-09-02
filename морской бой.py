import random

# Создание игровых досок
board_size = 6
player_ship_board = [['О' for _ in range(board_size)] for _ in range(board_size)]
player_attack_board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
computer_board = [['О' for _ in range(board_size)] for _ in range(board_size)]

# Расстановка кораблей на доске
def place_ship(board, size):
    while True:
        x = random.randint(0, board_size - 1)
        y = random.randint(0, board_size - 1)
        orientation = random.choice(['horizontal', 'vertical'])
        if is_valid_placement(board, x, y, orientation, size):
            if orientation == 'horizontal':
                for i in range(size):
                    board[y][x + i] = '■'
            else:
                for i in range(size):
                    board[y + i][x] = '■'
            break

def is_valid_placement(board, x, y, orientation, size):
    if orientation == 'horizontal':
        for i in range(size):
            if x + i >= board_size or board[y][x + i] != 'О':
                return False
    else:
        for i in range(size):
            if y + i >= board_size or board[y + i][x] != 'О':
                return False
    return True

for _ in range(4):
    place_ship(player_ship_board, 1)  # 4 корабля на одну клетку
for _ in range(2):
    place_ship(player_ship_board, 2)  # 2 корабля на две клетки
place_ship(player_ship_board, 3)  # 1 корабль на три клетки

for _ in range(4):
    place_ship(computer_board, 1)  # 4 корабля на одну клетку
for _ in range(2):
    place_ship(computer_board, 2)  # 2 корабля на две клетки
place_ship(computer_board, 3)  # 1 корабль на три клетки

# Функция отображения досок
def display_boards(ship_board, attack_board):
    print("   | 1 | 2 | 3 | 4 | 5 | 6 |")
    print("----------------------------")
    for i, (ship_row, attack_row) in enumerate(zip(ship_board, attack_board)):
        ship_row_display = [cell if cell == 'X' or cell == '■' else 'О' for cell in ship_row]
        print(f"{i+1} | {' | '.join(ship_row_display)} |  {i+1} | {' | '.join(attack_row)} |")

# Основной игровой цикл
player_turn = True

while True:
    if player_turn:
        print("Ваша доска:")
        display_boards(player_ship_board, player_attack_board)
        x = int(input("Введите номер столбца для атаки (1-6): ")) - 1
        y = int(input("Введите номер строки для атаки (1-6): ")) - 1

        if computer_board[y][x] == '■':
            print("Вы попали!")
            player_attack_board[y][x] = 'X'
            computer_board[y][x] = 'X'
        else:
            print("Промах!")
            player_attack_board[y][x] = 'P'
            player_turn = False
    else:
        print("Доска компьютера:")
        display_boards(computer_board, player_attack_board)
        x = random.randint(0, 5)
        y = random.randint(0, 5)

        if player_ship_board[y][x] == '■':
            print("Компьютер попал!")
            player_ship_board[y][x] = 'Y'
            player_attack_board[y][x] = 'Y'
        else:
            print("Компьютер промахнулся!")
            player_attack_board[y][x] = 'С'
            player_turn = True

    # Проверка на победу
    if all('■' not in row for row in computer_board):
        print("Вы победили!")
        break
    if all('■' not in row for row in player_ship_board):
        print("Компьютер победил!")
        break