# Импортируем модуль для работы с терминалом
import os

# Создаем двумерный массив для доски
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

# Определяем символы для игроков
X = "X"
O = "O"

# Определяем текущего игрока
current_player = X

def print_board():
    print("  1 2 3")
    print(" ┌─────┐")
    for i in range(3):
        print(f"{i+1}│{board[i][0]}│{board[i][1]}│{board[i][2]}│")
        if i < 2:
            print(" ├─┼─┼─┤")
    print(" └─────┘")

# Функция для проверки ввода игрока
def check_input(input):
    # Проверяем, что ввод состоит из двух цифр
    if len(input) != 2:
        return False
    # Проверяем, что ввод содержит только цифры от 1 до 3
    for char in input:
        if char not in "123":
            return False
    # Проверяем, что ячейка доски не занята
    row = int(input[0]) - 1
    col = int(input[1]) - 1
    if board[row][col] != " ":
        return False
    # Если все проверки пройдены, возвращаем True
    return True

# Функция для обновления доски согласно вводу игрока
def update_board(input):
    global board
    row = int(input[0]) - 1
    col = int(input[1]) - 1
    board[row][col] = current_player

# Функция для проверки победы
def check_win():
    global board
    # Проверяем горизонтальные линии
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
    # Проверяем вертикальные линии
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != " ":
            return True
    # Проверяем диагональные линии
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    # Если ни одна из линий не заполнена, возвращаем False
    return False

# Функция для проверки ничьи
def check_draw():
    global board
    # Проверяем, что все ячейки доски заняты
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    # Если все ячейки заняты, возвращаем True
    return True

# Функция для смены игрока
def switch_player():
    global current_player
    # Меняем символ игрока на противоположный
    if current_player == X:
        current_player = O
    else:
        current_player = X

# Функция для запуска игры
def play_game():
    global board
    global current_player
    # Выводим приветственное сообщение
    print("Добро пожаловать в игру в “Крестики-нолики”!")
    print("Для хода введите номер строки и столбца, например 11 или 23.")
    print("Ходит игрок", current_player)
    # Выводим доску на экран
    print_board()
    # Запускаем бесконечный цикл
    while True:
        # Получаем ввод от игрока
        user_input = input("Введите ваш ход: ")
        # Проверяем ввод на корректность
        if check_input(user_input):
            # Обновляем доску согласно вводу
            update_board(user_input)
            # Очищаем терминал
            os.system("cls")
            # Выводим доску на экран
            print_board()
            # Проверяем победу
            if check_win():
                # Выводим сообщение о победе
                print("Поздравляем! Игрок", current_player, "выиграл!")
                # Завершаем игру
                break
            # Проверяем ничью
            if check_draw():
                # Выводим сообщение о ничье
                print("Ничья! Никто не выиграл!")
                # Завершаем игру
                break
            # Меняем игрока
            switch_player()
            # Выводим сообщение о следующем ходе
            print("Ходит игрок", current_player)
        else:
            # Выводим сообщение об ошибке
            print("Неверный ввод! Попробуйте еще раз.")

# Запускаем игру
play_game()
