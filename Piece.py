import turtle
from Coordinates import white_screen_coordinates, neighbouring_points_def, point_definer

pieces_group = []


class Piece(turtle.Turtle):
    def __init__(self, x, y, piece_type, opposite_piece_type, ith_piece, radius):
        super().__init__()
        self.piece_type = piece_type
        self.number = ith_piece
        self.hideturtle()
        self.penup()
        self.goto(x, y - radius)
        self.pendown()
        self.begin_fill()
        self.color(opposite_piece_type, self.piece_type)
        self.circle(radius)
        self.end_fill()
        self.getscreen().onscreenclick(on_click)


def on_click(x1, y1):
    point_index = 0
    wn = pieces_group[0].getscreen()
    if wn < 300:
        square_len = wn / 6
    else:
        square_len = 50
    point_names = point_names = point_definer(square_len)
    valid_jump_points =
    for point in point_names:
        if abs(x1 - point.x) <= 10 and abs(y1 - point.y) <= 15:
            if point.state != 'empty':
                neighbouring_points = neighbouring_points_def(point_names)
                show_hint_moves(point_index, neighbouring_points, point_names, valid_jump_points)
                break
        point_index += 1


def show_hint_moves(point_index, neighbouring_points, point_names, valid_jump_points):
    can_move_neighbouring_points = []
    can_jump_moves = []
    for neighbouring_point in neighbouring_points[f'point_names[{point_index}]']:
        if neighbouring_point.state == 'empty':
            can_move_neighbouring_points.append(neighbouring_point)
        elif neighbouring_point.state != point_names[point_index].state:
            show_hint_jump_moves(point_index, valid_jump_points)


def show_hint_jump_moves(point_index, valid_jump_points):
    pass




'''    
    neighbouring_points = neighbouring_points_def()
    for piece in pieces_group:
        if abs(x1 - piece.xcor()) <= 10 and (15 >= y1 - piece.ycor() >= 0):
            # print(piece.xcor(), piece.ycor())
            show_hint_moves(piece, piece_position_index, neighbouring_points)
        piece_position_index += 1


# noinspection PyUnusedLocal
    print(neighbouring_points[piece_position_index])


def move(piece, point_names, neighbouring_points):
    print('the function "move" has been called')
    xth_coordinate_index = 0
    for coordinate in point_names:
        if piece.xcor() == coordinate.x and piece.ycor() == coordinate.y:
            for neighbouring_point in neighbouring_points['point_names[xth_coordinate_index]']:
                if neighbouring_point.state == 'empty':
                    grey_circle = turtle.Turtle
                    grey_circle.penup(piece)
                    grey_circle.goto(piece.xcor(), piece.ycor())
                    grey_circle.circle(piece, 5, 360)
        else:
            xth_coordinate_index += 1'''


def draw_pieces(radius, point_names):
    for i in range(32):
        x_coordinate = point_names[white_screen_coordinates()[i]].x
        y_coordinate = point_names[white_screen_coordinates()[i]].y
        arg3 = ['white', 'black']
        if i < 16:
            piece = Piece(x_coordinate, y_coordinate, arg3[0], arg3[1], i, radius)
            point_names[i].state = arg3[0]
        else:
            piece = Piece(x_coordinate, y_coordinate, arg3[1], arg3[0], i, radius)
            point_names[i].state = arg3[1]
        pieces_group.append(piece)
