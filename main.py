from warmuplogic import *

game_list = [0,1,2]
game_on = True

while game_on:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list, position)
    display_game(game_list)
    game_on = game_on_choice()