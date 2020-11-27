from PIL import Image, ImageTk
import turtle
import math
import json
from Config2 import *

# Window setup.

wn = turtle.Screen()
wn_len = 2500
wn_height = 1500
wn.title("Raja Raadh")
wn.bgcolor("lightblue")
wn.tracer(0)
wn.setup(wn_len, wn_height, 0, 0)

# Square length and triangle length.

# If checks if the window length is greater than or less than 720 and sets the square length accordingly.

if wn_height < 1500:
	square_len = wn_height / 10

# Else sets the square length to the maximum value of 120.

else:
	square_len = 150

triangle_len = math.sqrt(2 * square_len * square_len)

# Board.

board = None
board_brush_size = square_len / 10

# Game_ID and Game_ID_writer.

# Game_ID is the current game going on.

#game_ID = len(rdb)

game_ID_writer = turtle.Turtle()
game_ID_writer.hideturtle()
game_ID_writer.penup()

#game_ID_writer.goto(0, 4.5 * square_len)

#game_ID_writer.write(game_ID, True, align="center", font=("Arial", 15, "normal"))

# Valid_move_neighbouring_point_indices is just the list of indices of moves that a piece can move to.

valid_move_neighbouring_point_indices = []
draw_move_count = 0
draw_move_repetition_lists = [[], [], [], [], []]
list_to_add_move_in_draw_check = 0

# Jump stuff.

# Valid_jump_point_list_list is just the list of lists of indices of jumps that a piece can do and the kill points.

valid_jump_point_lists_list = []
valid_jump_point_lists_lists_list = []
current_iteration = []
jump = 0
jump_able_point = ""
to_moves = []
the_pieces_that_were_killed = []

# Is_selected is just a toggleable boolean. it is used for checking if the user has already clicked on a piece or not.

is_selected = False

# Pieces.

# Radius of pieces and the piece_types.

radius = int(square_len / 4)
piece_types = ["white", "black"]

# Adds pieces images.

black_piece = ImageTk.PhotoImage(Image.open("black piece.gif").resize((radius * 2, radius * 2)))
wn.addshape("black piece", turtle.Shape("image", black_piece))

white_piece = ImageTk.PhotoImage(Image.open("white piece.gif").resize((radius * 2, radius * 2)))
wn.addshape("white piece", turtle.Shape("image", white_piece))

# From Piece and from point.

from_piece = ""
from_point = ""

# Stamp maker.

stamp_maker = turtle.Turtle()
stamp_maker.hideturtle()
stamp_maker.penup()

# End of game screen object.

end_of_game_screen = turtle.Turtle()
end_of_game_screen.speed(0)
end_of_game_screen.setheading(90)

end_of_game_screen.shape("square")
end_of_game_screen.color("white")
end_of_game_screen.shapesize(50)

end_of_game_screen.penup()
end_of_game_screen.goto(0, -11 * square_len)

# End result writer.

end_result_writer = turtle.Turtle()
end_result_writer.hideturtle()
end_result_writer.goto(0, 2 * square_len)

# Grey dot maker.

grey_dot_maker = turtle.Turtle()
grey_dot_maker.color("black", "grey")
grey_dot_maker.hideturtle()
grey_dot_maker.penup()

# Game starts with white.

turns = ["white", "black"]
turn = "white"
