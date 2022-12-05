import random
import math


def count_new_position(old_position, move_, board_length):
    if move_ == "w":
        if old_position[1] == board_length - 1:
            return old_position
        else:
            return [old_position[0], old_position[1] + 1]
    elif move_ == "a":
        if old_position[0] == 0:
            return old_position
        else:
            return [old_position[0] - 1, old_position[1]]
    elif move_ == "s":
        if old_position[1] == 0:
            return old_position
        else:
            return [old_position[0], old_position[1] - 1]
    elif move_ == "d":
        if old_position[0] == board_length - 1:
            return old_position
        else:
            return [old_position[0] + 1, old_position[1]]
    else:
        return old_position


def count_length_from_player_to_key(player_pos, key_pos):
    return math.fabs(player_pos[0] - key_pos[0]) + math.fabs(player_pos[1] - key_pos[1])


def set_beginning_conditions(level):
    room_length = level * 10
    player_position = [0, 0]
    player_position[0] = random.randint(0, room_length - 1)
    player_position[1] = random.randint(0, room_length - 1)
    key_position = [0, 0]
    key_position[0] = random.randint(0, room_length - 1)
    key_position[1] = random.randint(0, room_length - 1)

    while key_position == player_position:
        key_position[0] = random.randint(0, room_length - 1)
        key_position[1] = random.randint(0, room_length - 1)

    return room_length, player_position, key_position


def run_game(level):
    room_length, player_position, key_position = set_beginning_conditions(level)
    length_from_player_to_key = count_length_from_player_to_key(player_position, key_position)
    number_of_moves = 0

    print("Zaczynamy grę! Poruszasz się klawiszami <w a s d>")

    while key_position != player_position:
        player_move = input("Twój ruch: ")
        if player_move not in ["w", "a", "s", "d"]:
            print("Wpisałeś złą opcję. Spróbuj jeszcze raz")
            continue
        number_of_moves += 1
        previous_player_position = player_position
        player_position = count_new_position(player_position, player_move, room_length)

        if player_position == previous_player_position:
            print("Ściana! Zostajesz w tym samym miejscu \n")
        else:
            previous_length_from_player_to_key = length_from_player_to_key
            length_from_player_to_key = count_length_from_player_to_key(player_position, key_position)

            if length_from_player_to_key == 0:
                break
            elif length_from_player_to_key > previous_length_from_player_to_key:
                print("Zimniej! \n")
            else:
                print("Cieplej! \n")
    print("Gorąco! Znalazłeś klucz w", number_of_moves, "ruchach.\n")


    run_start_menu()


def select_game_level():
    selected_level = input("Wybierz poziom gry: \n 1 - łatwy \n 2 - średni \n 3 - trudny\n")
    if selected_level in ["1", "2", "3"]:
        return int(selected_level)
    else:
        print("Wybrany poziom nie istnieje. Wybierz jeszcze raz.\n")
        return select_game_level()


def run_start_menu():
    choice = input("Wpisz wybraną opcję i zatwierdź Enterem: \n n - Nowa Gra \n i - Instrukcja \n q - Quit (Wyście) \n")

    if choice == "n":
        selected_level = select_game_level()
        run_game(selected_level)

    elif choice == "i":
        print("\n"
              "INSTRUKCJA GRY: \n"
              "Jesteś w ciemnym kwadratowym pomieszczeniu. Możesz poruszać się po nim, robiąc jeden krok: \n"
              "do przodu (wybierz klawisz 'w'), \n"
              "w lewo (wybierz klawisz 'a'), \n"
              "do tyłu (wybierz klawisz 's'),\n"
              "w prawo (wybierz klawisz 'd'). \n"
              "Mały chochlik ukrył klucz do wyjścia gdzieś w pomieszczeniu. Zaprasza Cię do zabawy w ciepło - zimno \n"
              "(gdy zbliżysz się do klucza, będzie <cieplej>, a gdy się oddalisz - <zimniej>).\n")
        run_start_menu()
    elif choice == "q":
        print("Do zobaczenia!\n")
        return
    else:
        print("Wybrana opcja nie istnieje. Wybierz jeszcze raz.\n")
        run_start_menu()
    return



