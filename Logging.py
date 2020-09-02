def logger(list_of_moves, game_number):
    new_log_file = open(f'new_log_file{game_number}.txt', 'w')
    new_log_file.write(list_of_moves)
