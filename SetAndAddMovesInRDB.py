
import json

game_structure = {
	"Game_ID": 0,
	"Result": "",
	"Moves": []
}
move_structure = {
	"From_Move": "",
	"To_Moves": [
		""
	],
	"Killed_Pieces": [
		""
	]
}

# Returns nothing. Takes information and puts in the database by calling the function set_game_properties.

def set_move(game_ID:int, rdb:list, from_move:str, to_moves:list, result:str="IP", killed_pieces:list=[]):
 	
 	# Try checks if the game already exists or not and if it doesnt it goes in the except.
 	
 	try:
 		rdb[game_ID]
 	
 	# If it goes in the except it means that the game does not exist, and that this is the first move. It creates another game in the game_structure format.
 	
 	except IndexError:
 		rdb.append(game_structure)
 	set_game_properties(rdb, game_ID, result, from_move, to_moves, killed_pieces)


def get_moves(rdb:list, game_ID:int):
	try:
		return rdb[game_ID]["Moves"]
	except IndexError:
		return []


# The function sets the properties of the game in the database by taking the required information.

def set_game_properties(rdb, game_ID, result, from_move, to_moves, killed_pieces):
	
	# Current game is the game of which the properties are being set.
	
	current_game = rdb[game_ID]
	current_game["Game_ID"] = game_ID
	current_game["Result"] = result
	
	# Appends a copy of move_structure
	
	current_game["Moves"].append(move_structure)
	
	# It then fills the values in the corresponding places
	
	current_game["Moves"][len(current_game["Moves"]) - 1]["From_Move"] = from_move
	current_game["Moves"][len(current_game["Moves"]) - 1]["To_Moves"] = to_moves
	current_game["Moves"][len(current_game["Moves"]) - 1]["Killed_Pieces"] = killed_pieces


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
#temp_database_of_games_as_json = json.loads(temp_database_of_games)
#temp_database_of_games_as_python = json.dumps(temp_database_of_games_as_json, indent=2)
#set_move(1, temp_database_of_games, "W12",["17"])
#get_moves(temp_database_of_games, 4)
#print(temp_database_of_games_as_python)