from welcome import greet_user
from noc import play_game
from geo import play_geometric_progression_game


def choose_game():
    print("Выберите игру:")
    print("1 - Игра 'NOC'")
    print("2 - Игра 'Геометрическая прогрессия'")
    choice = input("Введите номер игры (1 или 2): ")
    while choice not in ['1', '2']:
        print("Некорректный выбор. Пожалуйста, введите 1 или 2.")
        choice = input("Введите номер игры (1 или 2): ")
    return choice


def play_rounds(name, game_func):
    for round_num in range(1, 4):
        print(f"\nРаунд {round_num}:")
        game_func(name)
    print(f"\nИгра завершена, {name}!")


def main():
    name = greet_user()  
    game_choice = choose_game() 

    if game_choice == '1':
        print(f"Вы выбрали игру 'NOC'. Удачи, {name}!")
        play_rounds(name, play_game)  # Играем 3 раунда в игру NOC
    elif game_choice == '2':
        print(f"Вы выбрали игру 'Геометрическая прогрессия'. Удачи, {name}!")
        play_rounds(name, play_geometric_progression_game)


if __name__ == "__main__":
    main()
