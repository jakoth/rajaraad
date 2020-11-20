from Config2 import *
import json


# Returns nothing. Takes information and puts in the database by calling the function set_game_properties.

def set_move(game_ID:int, from_piece:any, to_moves:list, killed_pieces:list=[], result:str="IP"):
 	
 	# Try checks if the game already exists or not and if it doesnt it goes in the except.
 	
 	try:
 		rdb[game_ID]
 	
 	# If it goes in the except it means that the game does not exist, and that this is the first move. It creates another game in the game_structure format.
 	
 	except IndexError:
 		rdb.append(game_structure)
 	
 	set_game_properties(game_ID, result, from_piece, to_moves, killed_pieces)
 	"""
 	with open("Database.json", "w"):
 		json.dump(rdb)"""


# Returns the moves of a particular game. If no game is found, it returns an empty list.

def get_moves(game_ID:int):
	
	try:
		return rdb[game_ID]["Moves"]
	
	except IndexError:
		return []


# Returns nothing. The function sets the properties of the game in the database by taking the required information.

def set_game_properties(game_ID, result, from_piece, to_moves, killed_pieces):
	
	# Current game is the game of which the properties are being set.
	
	current_game = rdb[game_ID]
	current_game["Game_ID"] = game_ID
	current_game["Result"] = result
	
	# Appends a copy of move_structure.
	
	current_game["Moves"].append(move_structure)
	
	# Current move is the move in which it is filling the values. It then fills the values in the corresponding places.
	
	current_move = current_game["Moves"][len(current_game["Moves"]) - 1]
	current_move["From_Piece"] = from_piece
	current_move["To_Moves"] = to_moves
	current_move["Killed_Pieces"] = killed_pieces


temp_database_of_games = [
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
	}
]
{
	"PositionId":"1",
	"Name":"A1",
	"PieceName":"W",
	"ToPositionId":["2","4"],
	"JumpPositionId":["3","9"]
}
