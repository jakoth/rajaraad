from Config2 import *
import Config2
import random
from SetAndAddMovesInRDB import get_moves
from Piece import *


def cpu_level_noobiest():
	
	# Select random piece and play a random move.
		
	# Call valid move in for loop which should return the list of valid moves then take the first valid move to go to.
		
	pass


# Returns the best move, given the database, game_ID, what is the cpu playing for(white or black) and lastly the possible moves for each pice respectively.

def cpu_level_extreme(game_ID:int, cpu_side:str="black"):
	
	default_move = ""
	default_rating = -100000
	current_game_state = get_moves(game_ID)
	possible_moves = calc_all_possible_moves(cpu_side)
	
	# For loop takes each game in the database.
	
	for game in rdb:
		
		# If statement checks if the game has more moves than what have been played and if the moves that are played are in the game.
		
		if len(game["Moves"]) > len(current_game_state) and current_game_state == game["Moves"][0:len(current_game_state)]:
			new_game_result = game["Result"]
			
			# The CPU is playing as black as default. If it is white then it switches the result.
			
			if cpu_side == "white":
				
				if game["Result"] == "W":
					new_game_result = "L"
					
				elif game["Result"] == "L":
					new_game_result = "W"
			
			# Finds the next game move in the game in the RDB
			
			next_game_move = game["Moves"][len(current_game_state)]
			
			for move in possible_moves.items():
			
			# If checks if the next move is in the possible moves. Also this is there so that all the moves are rated and not only the moves that are played before are rated.
			
				if move[0] == next_game_move:
					move[0] = move[0]
				
					# If checks if the result of the game was a loss or not then rates accordingly.
				
					if new_game_result == "W":
						possible_moves[move[0]] += 1
						
					elif new_game_result == "L":
						possible_moves[move[0]] -= 1
	
	# For loop takes the move with the best rating and stores it in the variable "default_move".
	
	for move, move_rating in possible_moves.items():
		
		# If checks if the move has greater rating than the "default_rating". If yes, then it reassign the value of the "default_rating" to the moves rating. 
		
		if move_rating > default_rating:
			default_move = move
			default_rating = move_rating
	
	return default_move


#print(cpu_level_extreme(1, "White"))
