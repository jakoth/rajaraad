import json
import Database

# Points and pieces.

# All the pieces and coordinates are in these lists.

point_names = []
pieces_group = []
white_pieces_group = []
black_pieces_group = []

# RDB.

# All games in the RDB will be in the game structure.

game_structure = {
	"Game_ID": 0,
	"Result": "",
	"Moves": []
}

# All the moves in a game will be in the move structure.

move_structure = {
	"From_Piece_": "",
	"To_Moves": [
		""
	],
	"Killed_Pieces": [
		""
	]
}

# Temporary database. RDB to be replaced with the RDB on the SQL server.
"""
with open("Database.json") as RDB:
	rdb = json.load(RDB)"""
