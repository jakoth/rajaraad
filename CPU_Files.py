import random
from SetAndAddMovesInRDB import get_moves

temp_rdb = [
	{
		"Game_ID": 0,
		"Result": "W",
		"Moves": [
			{
				"From_Move": "W12",
				"To_Move": [
					"17"
				],
				"Killed_Piece": [
					""
				]
			}
		]
	},
	{
		"Game_ID": 1,
		"Result": "W",
		"Moves": [
			{
				"From_Move": "W12",
				"To_Move": [
					"17"
				],
				"Killed_Piece": [
					""
				]
			},
			{
				"From_Move": "W12",
				"To_Move": [
					"17"
				],
				"Killed_Piece": [
					""
				]
			},
			{
				"From_Move": "W12",
				"To_Move": [
					"17"
				],
				"Killed_Piece": [
					""
				]
			},
			{
				"From_Move": "W12",
				"To_Move": [
					"17"
				],
				"Killed_Piece": [
					""
				]
			},
			{
				"From_Move": "W12",
				"To_Move": [
					"17"
				],
				"Killed_Piece": [
					""
				]
			}
		]
	}
]
temp_current_game_state = [
	1,
	2,
	3
]
temp_possible_moves = {
	'4' : 0,
	'5': 0
}

def cpu_level_noobiest():
	
	# Select random piece and play a random move
		
		# Call valid move in for loop which should return the list of valid moves then take the first valid move to go to
		
	pass

# Returns the best move, given the database, game_ID, what is the cpu playing for(white or black) and lastly the possible moves for each pice respectively

def cpu_level_extreme(rdb:list, game_ID:int, possible_moves_for_each_piece, cpu_side:str="Black"):
	
	# Access database and put value in a variable named "rdb"
	
	possible_moves_for_each_piece_copy = possible_moves_for_each_piece
	default_move = ""
	default_rating = -100000
	current_game_state = get_moves(rdb, game_ID)
	
	# Takes each game in the database
	
	for game in rdb:
		
		# If statement checks if the game has more moves than what have been played and if the moves that are played are in the game
		
		if len(game["Moves"]) > len(current_game_state) and current_game_state == game["Moves"][0:len(current_game_state)]:
			new_game_result = game["Result"]
			
			# The CPU is playing as black as default. If it is white then it switches the result.
			
			if cpu_side == "White":
				if game["Result"] == "W":
					new_game_result = "L"
				elif game["Result"] == "L":
					new_game_result = "W"
			next_game_move = game["Moves"][len(current_game_state)]
			
			for move in possible_moves_for_each_piece_copy.items():
			
			# Checks if the next move is in the possible move. Also this is there so that all the moves are rated and not only the moves that are played before are rated.
			
				if move[0] == next_game_move:
					move[0] = move[0]
				
					# Checks if the result of the game was a loss or not then rates accordingly
				
					if new_game_result == "W":
						possible_moves_for_each_piece_copy[move[0]] += 1
					elif new_game_result == "L":
						possible_moves_for_each_piece_copy[move[0]] -= 1
	
	# For loop takes the move with the best rating and stores it in the variable "default_move"
	
	for move, move_rating in possible_moves_for_each_piece_copy.items():
		if move_rating > default_rating:
			default_move = move
			default_rating = move_rating
	return default_move		

print(cpu_level_extreme(temp_rdb, 1, temp_possible_moves, "White"))
