def display_game(game_list):
    print(game_list)

def position_choice():
    choice = "Wrong"
    while choice not in ["0","1","2"]:
        choice = input("Enter the Position No. to change: ")
        if choice not in ["0","1","2"]:
            print("Sorry! Invalid Input. \nPlease select the Position No. from (0-2).")
    return int(choice)

def replacement_choice(game_list, position):
    user_choice = input("Enter any string to put on Position No. {}: ".format(position))
    
    game_list[position] = user_choice
    return game_list

def game_on_choice():
    choice = "Wrong"
    while choice not in ["Y","N"]:
        choice = input("Do you want to play again? (Y / N): ")
        if choice not in ["Y","N"]:
            print("Sorry! Invalid Input. Enter 'Y' for Yes and 'N' for No.")
    if choice != 'N':
        return True
    else:
        return False


