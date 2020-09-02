import turtle
from Coordinates import point_definer, white_screen_coordinates, neighbouring_points_def
from Board import Board
from Piece import draw_pieces


def raja_raad_init():
    wn = turtle.Screen()
    wn_len = 300
    wn_height = 600
    wn.title("Raja Raad")
    wn.bgcolor("lightblue")
    wn.tracer(0)
    wn.setup(wn_len, wn_height)
    if wn_len < 300:
        square_len = wn_len / 6
    else:
        square_len = 50
    point_names = point_definer(square_len)
    neighbouring_points_def(point_names)
    white_screen_coordinates()
    # noinspection PyUnusedLocal
    board1 = Board("orange", square_len, "red", "blue")
    draw_pieces(10, point_names)
    while True:
        wn.update()


raja_raad_init()
