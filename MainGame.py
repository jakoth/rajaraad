from config import *
import turtle
from Coordinates import *
from Board import Board
from Piece import draw_pieces, on_click
from CPU_Files import *


# Driver function.

# Returns nothing. Temporarily is the function which calls everything in order. May be replaced by another function. 

def raja_raad_init():
	
	point_definer()
	neighbouring_points_def()
	white_screen_coordinates()
	board1 = Board("orange", config.board_brush_size, "red", "blue")
	draw_pieces()
	wn.onscreenclick(on_click)
	
	while True:
		wn.update()


raja_raad_init()
