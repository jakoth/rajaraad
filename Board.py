import turtle
import math


def drawpoly(n, length, direct, board):
    for i in range(n):
        board.rt(360 / n)
        if direct:
            board.backward(length)
        else:
            board.forward(length)


def draw_line(start_pos, length, direction_angle, board, line_colour):
    board.penup()
    board.goto(start_pos[0], start_pos[1])
    board.pendown()
    board.color(line_colour)
    board.setheading(direction_angle)
    board.forward(length)


def draw_x(start_pos, length, board, line_colour_up, line_colour_down):
    draw_line(start_pos, length, 45, board, line_colour_up)
    draw_line(start_pos, length, 135, board, line_colour_up)
    draw_line(start_pos, length, 225, board, line_colour_down)
    draw_line(start_pos, length, 315, board, line_colour_down)


def new_board(board_colour, square_len, triangle_color_up, triangle_color_down):
    triangle_len = math.sqrt(2 * square_len * square_len)
    board = turtle.Turtle()
    board.hideturtle()
    board.speed(0)
    board.pensize(5)
    board.color(board_colour)
    board.penup()
    board.goto(-2 * square_len, -2 * square_len)
    board.pendown()
    # Centre Square
    for x in range(1, 5):
        drawpoly(4, x * square_len, True, board)
    board.penup()
    board.goto(2 * square_len, 2 * square_len)
    board.pendown()
    for x in range(1, 5):
        drawpoly(4, x * square_len, False, board)
    # draw lines
    draw_x([0, -2 * square_len], 2 * triangle_len, board, board_colour, triangle_color_down)
    draw_x([0, 2 * square_len], 2 * triangle_len, board, triangle_color_up, board_colour)
    draw_line([0, 2 * square_len], 2 * square_len, 90, board, triangle_color_up)
    draw_line([-1 * square_len, 3 * square_len], 2 * square_len, 0, board, triangle_color_up)
    draw_line([-2 * square_len, 4 * square_len], 4 * square_len, 0, board, triangle_color_up)
    draw_line([0, -2 * square_len], 2 * square_len, 270, board, triangle_color_down)
    draw_line([-1 * square_len, -3 * square_len], 2 * square_len, 0, board, triangle_color_down)
    draw_line([-2 * square_len, -4 * square_len], 4 * square_len, 0, board, triangle_color_down)


class Board:
    def __init__(self, board_colour, background_color, triangle_color_up, triangle_color_down):
        new_board(board_colour, background_color, triangle_color_up, triangle_color_down)
