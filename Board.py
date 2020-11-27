import turtle
from config import *
import config


# Returns nothing. Draws a poly based on the number of sides the length of one side and the direction and a turtle object.

def drawpoly(number_of_sides, length, move_forward, turtle_obj):
	
	# For loop is for the number of sides in the poly.
	
	for i in range(number_of_sides):
		
		# If checks if the direction to move is forwards or backwards.
		
		if move_forward:
			turtle_obj.forward(length)
		
		else:
			turtle_obj.backward(length)
		
		turtle_obj.lt(360 / number_of_sides)


# Returns nothing. Draws a line, given the starting position, the length of the line, the direction in which the line must be drawn and a turtle object.

def draw_line(start_pos, length, direction_in_angle, turtle_obj):
	
	# Goes to the start_pos.
	
	turtle_obj.penup()
	turtle_obj.goto(start_pos[0], start_pos[1])
	turtle_obj.pendown()
	
	# Sets heading according to "direction_in_angle" and goes forward according to the length
	
	turtle_obj.setheading(direction_in_angle)
	turtle_obj.forward(length)


# Returns nothing. Draws an x shape, given the starting position, the length of the lines (4) of the x, a turtle object and the colour of the top left, top right, bottom left and the bottom right lines.

def draw_x(start_pos, length, turtle_obj, line_colour_top_left, line_colour_top_right, line_colour_bottom_left, line_colour_bottom_right):
	
	# Top right line.
	
	turtle_obj.color(line_colour_top_right)
	draw_line(start_pos, length, 45, turtle_obj)
	
	# Top left line.
	
	turtle_obj.color(line_colour_top_left)
	draw_line(start_pos, length, 135, turtle_obj)
	
	# Bottom left line.
	
	turtle_obj.color(line_colour_bottom_left)
	draw_line(start_pos, length, 225, turtle_obj)
	
	# Bottom right line.
	
	turtle_obj.color(line_colour_bottom_right)
	draw_line(start_pos, length, 315, turtle_obj)


# All boards will be an instance of the Board class.

class Board(turtle.Turtle):
	
	def __init__(self, board_colour, brush_size, triangle_color_up, triangle_color_down):
		
		super().__init__()
		
		# Sets the board in config to itself.
		
		config.board = self
		
		# Initialises the properties.
		
		self.colour = board_colour
		self.line_thickness = brush_size
		self.triangle_color_up = triangle_color_up
		self.triangle_color_down = triangle_color_down
		
		# Draws the board.
		
		self.new_board()
	
	# Returns nothing. Creates a new board.
	
	def new_board(self):
		
		# Sets self's properties.
		
		self.hideturtle()
		self.speed(0)
		self.pensize(self.line_thickness)
		self.color(self.colour)		
		
		# Centre Square.
		
		# Goes to the bottom left of the square of the board.
		
		self.penup()
		self.goto(-2 * square_len, -2 * square_len)
		self.pendown()
		
		# For loop makes the board in squares (small to big). The sizes are determined by x.
		
		for x in range(1, 5):
			drawpoly(4, x * square_len, True, self)
		
		# Goes to the top right of the square of the board.
		
		self.penup()
		self.goto(2 * square_len, 2 * square_len)
		self.pendown()
		
		# For loop makes the board in squares (small to big). The sizes are determined by x. But this time the direction is reversed.
		
		for x in range(1, 5):
			drawpoly(4, x * square_len, False, self)
		
		# Draws Triangles.
		
		# Draws the diamond in the center and the side lines of the triangle.	
		
		draw_x([0, -2 * square_len], 2 * triangle_len, self, self.colour, self.colour, self.triangle_color_down, self.triangle_color_down)
		draw_x([0, 2 * square_len], 2 * triangle_len, self, self.triangle_color_up, self.triangle_color_up, self.colour, self.colour)
		
		# Draws the vertical line and then horizontal line of the plus and then the top line of the top triangle.
		
		self.color(self.triangle_color_up)
		draw_line([0, 2 * square_len], 2 * square_len, 90, self)
		draw_line([-1 * square_len, 3 * square_len], 2 * square_len, 0, self)
		draw_line([-2 * square_len, 4 * square_len], 4 * square_len, 0, self)
		
		# Draws the vertical line and then horizontal line of the plus and then the bottom line of the bottom triangle.
		
		self.color(self.triangle_color_down)
		draw_line([0, -2 * square_len], 2 * square_len, 270, self)
		draw_line([-1 * square_len, -3 * square_len], 2 * square_len, 0, self)
		draw_line([-2 * square_len, -4 * square_len], 4 * square_len, 0, self)
