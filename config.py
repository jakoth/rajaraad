import turtle
import math

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
rdb = [
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
point_names = []
pieces_group = []
wn = turtle.Screen()
wn_len = 1500
wn_height = 1200
wn.title("Raja Raad")
wn.bgcolor("lightblue")
wn.tracer(0)
wn.setup(wn_len, wn_height)
if wn_len < 720:
	square_len = wn_len / 6
else:
	square_len = 120
triangle_len = math.sqrt(2 * square_len * square_len)
radius = 25
