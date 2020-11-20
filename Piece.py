import config
from config import *
from Coordinates import *
import Config2
#from SetAndAddMovesInRDB import set_move


# All the white and the black pieces will be an instance of the class Piece.

class Piece(turtle.Turtle):
	
	def __init__(self, x, y, piece_type, opposite_piece_type, ith_piece, point):
		
		super().__init__()
		
		# Sets default properties.
		
		self.piece_type = piece_type
		self.opposite_piece_type = opposite_piece_type
		self.number = ith_piece
		
		# Piece goes to the position it is supposed to.
		
		self.penup()
		self.goto(x, y)
		
		# Draws the pieces.
		
		self.shape(f"{self.piece_type} piece")
		point.piece = self


# Returns nothing. Gets called when clicked on the screen.

def on_click(x1, y1):
	
	# For loop takes each point in the point_names i.e. the list of all points.
	
	for point in point_names:
		
		# If checks if the player clicked on a piece or anywhere else.
		
		if abs(x1 - point.x) <= radius + 5 and abs(y1 - point.y) <= radius + 5:
			
			# If checks if the user has already clicked on a piece or not.
			
			if not config.is_selected:
				
				# It checks if the player had jumped before.
				
				if config.jump_able_point:
					
					# If he had jumped before it checks if the point he has clicked is the same point on which he had jumped earlier.
					
					if point.name != config.jump_able_point.name:
						
						# If not, it returns.
						
						return
				
				# If the state of the point is not empty, then it calls the show_valid_moves function.
				
				if point.state == config.turn:
					
					# Checks if a jump had been made in the previous move.
					
					if config.jump:
						
						# Shows only the possible jumps.
						
						game_ID_writer.write(config.is_selected, True, align="center", font=("Arial", 15, "normal"))
						show_hint_moves(point, True)
					
					# If not, then shows all the moves including the normal moves.
					
					else:
						
						# Shows all the possible moves.
						
						show_hint_moves(point)
					
					# Sets the from point and from piece.
					
					config.from_point = point
					config.from_piece = point.piece
					
					# Flips the boolean.
					
					config.is_selected = True
					
					# Break is for the outermost loop.
					
					break
			
			# If it is in else it means that the player clicked on a piece before.
			
			else:
				
				# If checks if a jump had been made.
				
				if not config.jump:
					
					# For takes each index of the point in the valid moves list of the from piece.
					
					for index in config.valid_move_neighbouring_point_indices:
						
						# If checks if the clicked point is in the valid points to move. 
						
						if point.name == point_names[index].name:
							
							# Moves the piece and adds a count to the draw_move_count and adds the move to the appropriate list.
							
							move(config.from_piece, config.from_point, point, grey_dot_maker)
							config.draw_move_count += 1
							add_move_to_correct_draw_move_list(config.from_point, point)
							
							# Flips the boolean is_selected and the turn.
							
							config.is_selected = False
							flip_turn()
							'''
							# Sets the move in RDB.
							
							set_move(game_ID, config.from_piece, [point])'''
							
							# Checks if the game has ended.
							
							if check_game_end() != "IP":
								end_of_game(check_game_end()[0], check_game_end()[1])
				
				# For takes each list of the point in the valid_jump_point_lists_list list of the from piece.
				
				for valid_jump_point_list in config.valid_jump_point_lists_list:
					
					# Jump_point_index is the index of the point onto which the piece can jump and the kill_point_index is the index of the point of which the piece will be killed.
					
					jump_point_index = valid_jump_point_list[1]
					kill_point_index = valid_jump_point_list[0]
					
					# If checks if the clicked point is in the valid points to move. 
					
					if point.name == point_names[jump_point_index].name:
						
						# Sets the kill piece.
						
						kill_piece = point_names[kill_point_index].piece
						
						# Makes the piece jump.
						
						jump(config.from_piece, config.from_point, kill_piece, point_names[kill_point_index], point, grey_dot_maker)
						
						# Checks if there are more jumps possible with the same piece.
						
						if check_valid_hint_jump_moves(point):
							
							# If there are more jumps, then it calls the function again to show more jump moves.
							
							config.jump_able_point = point
							config.jump += 1
							config.is_selected = False
							on_click(x1, y1)
						
						else:
							
							# Else, it resets the jump and jump_able_piece and flips the boolean is_selected and the turn.
							
							config.draw_move_count = 0
							config.jump_able_point = ""
							config.jump = 0
							config.is_selected = False
							flip_turn()
							
							"""# Sets the jump in RDB.
							
							set_move(game_ID, config.from_piece, config.to_moves, config.the_pieces_that_were_killed)
							config.to_moves = []
							config.the_pieces_that_were_killed = []"""
							
							# Checks if the game has ended.
							
							if check_game_end() != "IP":
								end_of_game(check_game_end()[0], check_game_end()[1])
				
				# If it is not a valid point then it checks if the user clicked on the same piece again.
				
				if point.name == config.from_point.name:
					
					# It resets the hints.
					
					grey_dot_maker.clear()
					
					# Flips the boolean is_selected.
					
					config.is_selected = False
				
				# If none of the above conditions are it checks if the state of the point is the same as the from position.
				
				elif point.state == config.from_point.state:
					
					# Flips the boolean is_selected and calls the function again for the piece that the player clicked.
					
					config.is_selected = False
					on_click(x1, y1)


# Returns nothing. Gets called if the user clicked on a piece.

def show_hint_moves(point, show_only_hint_jump_moves=False):
	
	# Resets the hints.
	
	grey_dot_maker.clear()
	
	# If checks if the player hadn't jumped before and if he didn't it shows the hint moves as well.
	
	if not show_only_hint_jump_moves:
		
		# For loop takes each valid move and makes a grey dot on that coordinate.
		
		for valid_move_point_index in check_valid_hint_moves(point):
			
			# Goes to the place to make the grey dot.
			
			grey_dot_maker.goto(point_names[valid_move_point_index].x, point_names[valid_move_point_index].y - radius)
			
			# Makes a grey dot where the piece can move.
			
			grey_dot_maker.pendown()
			
			grey_dot_maker.begin_fill()
			grey_dot_maker.circle(radius)
			grey_dot_maker.end_fill()
			
			grey_dot_maker.penup()
	
	# For loop takes each jump list and makes a grey dot on the jump point (2 element of the list).
	
	for jump_point_list in check_valid_hint_jump_moves(point):
		
		# Jump_point_index is the index of the point onto which the piece can jump.
		
		jump_point_index = jump_point_list[1]
		
		# Goes to the place to make the grey dot.
		
		grey_dot_maker.goto(point_names[jump_point_index].x, point_names[jump_point_index].y - radius)
		
		# Makes a grey dot where the piece can jump.
		
		grey_dot_maker.pendown()
		
		grey_dot_maker.begin_fill()
		grey_dot_maker.circle(radius)
		grey_dot_maker.end_fill()
		
		grey_dot_maker.penup()


# Returns the list of indices of valid moves of a point.

def check_valid_hint_moves(point):
	
	# Resets the list.
	
	config.valid_move_neighbouring_point_indices = []
	
	# For loop takes each index of the neighbouring points of the point.
	
	for neighbouring_point in neighbouring_points_def()[point]:
		
		# If checks if the state of the neighbouring_point is empty and if it is, then it appends it to the valid_move_neighbouring_point_indices list. 
		
		if point_names[neighbouring_point].state == "empty":
			config.valid_move_neighbouring_point_indices.append(neighbouring_point)
			continue
	
	return config.valid_move_neighbouring_point_indices


# Returns the list of lists of indices of kill points and valid jump points.

def check_valid_hint_jump_moves(point):
	
	# Resets the list.
	
	config.valid_jump_point_lists_list = []
	
	# For takes each list in the valid_jump_moves_def function.
	
	for jump_point_list in valid_jump_moves_def()[point]:
		
		# Jump point index is the index of the point where the piece will be able to jump to if it is verified and kill point index is the point of which the piece will be killed if verified.
		
		jump_point_index = jump_point_list[1]
		kill_point_index = jump_point_list[0]
		
		# If checks if the kill point index is not empty and not the state of the point.
		
		if point_names[kill_point_index].state != point.state and point_names[kill_point_index].state != "empty" and point_names[jump_point_index].state == "empty":
			
			# If it is in the if it means it is verified so it appends it to the valid jump point list.
			
			config.valid_jump_point_lists_list.append(jump_point_list)
	
	return config.valid_jump_point_lists_list


# Returns the tuple of lists of lists of indices of points of kill and jump points. 

def check_all_valid_hint_jump_moves(point, outside_call=True):
	
	# If checks if the function is being call the first time (from outside) or from inside the function.
	
	if outside_call:
		
		# If it is being called from outside the function, it resets the lists.
		
		config.valid_jump_point_lists_lists_list = []
		config.current_iteration = []
	
	# For takes each valid point filtered from the valid_jump_moves_def function by the check_valid_hint_jump_moves function. 
	
	for valid_jump_point_list_indices in check_valid_hint_jump_moves(point):
		
		# For takes each list in the config.current_iteration list. 
		
		for jump_list in config.current_iteration:
			
			# If checks if the kill point of the current valid_jump_point_list_indices is in the current jump_list.
			
			if valid_jump_point_list_indices[0] == jump_list[0]:
				break
		
		# If the kill point of the current valid_jump_point_list_indices is not in the current jump_list then it proceeds.
		
		else:
			
			# Appends the valid_jump_point_list_indices in the config.current_iteration. 
			
			config.current_iteration = config.current_iteration + [valid_jump_point_list_indices]
			
			# Appends config.current_iteration into the config.valid_jump_point_lists_lists_list.
			
			config.valid_jump_point_lists_lists_list.append(config.current_iteration)
			
			# Jump_point_index is the index onto which the piece can jump.
			
			jump_point_index = valid_jump_point_list_indices[1]
			
			# Proceeds to find more jumps.
			
			check_all_valid_hint_jump_moves(point_names[jump_point_index], False)
			
			# Removes the last item in the config.current_iteration list. 
			
			config.current_iteration = config.current_iteration[0:-1]
	
	# If the function is being called from outside, it returns the config.valid_jump_point_lists_lists_list.
	
	if outside_call:
		return config.valid_jump_point_lists_lists_list


# Returns all the possible moves for a side.

def calc_all_possible_moves(side):
	
	possible_moves = {}
	
	# For loop takes each point existing.
	
	for point in point_names:
		
		# If statement checks if there is a piece on the point and if it belongs to the same side.
		
		if point.piece and point.piece.piece_type == side:
			
			# Checking all the moves.
			
			# For loop takes all the possible valid moves.
			
			for valid_move_index in check_valid_hint_moves(point):
				
				# Then it adds it to the possible moves in the move notation format (from_point, to_point).
				
				move_notation = (point, point_names[valid_move_index])
				possible_moves[move_notation] = 0
			
			# Checking all the jumps.
			
			# For loop takes each branch of the possible branches of jumps.
			
			for jump_branch in check_all_valid_hint_jump_moves(point):
				
				# Then it adds it to the possible moves in the jump notation format (from_point, [[kill_point_index, to_point_index]]).
				
				jump_notation = (point, jump_branch)
				possible_moves[jump_notation] = 0
	
	return possible_moves


# Returns nothing. Moves the from_piece to the to_point.

def move(from_piece, from_point, to_point, hint_turtle_obj):
	
	# Sets the state of the point onto which the piece has moved.
	
	to_point.state = from_point.state
	to_point.piece = from_point.piece
	
	# Resets the hints and also sets the state and piece (that is on it) of the from point to empty.
	
	hint_turtle_obj.clear()
	from_point.state = "empty"
	from_point.piece = ""
	
	# Makes the piece move.
	
	from_piece.goto(to_point.x, to_point.y)


# Returns nothing. Makes the piece jump over another piece and kill the kill piece.

def jump(from_piece, from_point, kill_piece, kill_point, to_point, hint_turtle_obj):
	
	config.to_moves.append(to_point)
	config.the_pieces_that_were_killed.append(kill_piece)
	
	# Sets the state of the point onto which the piece has moved.
	
	to_point.state = from_point.state
	to_point.piece = from_point.piece
	
	# Resets the hints and the kill piece and also sets the state of the from point and kill point to empty.
	
	hint_turtle_obj.clear()
	
	from_point.state = "empty"
	from_point.piece = ""
	
	kill_point.state = "empty"
	kill_point.piece = ""
	kill_piece.hideturtle()
	
	# Removes kill piece from any list to which it belongs and then deletes it.
	
	pieces_group.remove(kill_piece)
	
	if kill_piece.piece_type == "white":
		white_pieces_group.remove(kill_piece)
	
	else:
		black_pieces_group.remove(kill_piece)
	
	del kill_piece
	
	# Makes the piece jump.
	
	from_piece.goto(to_point.x, to_point.y)


# Return nothing. Adds the move to the appropriate list.

def add_move_to_correct_draw_move_list(from_point, to_point):

	config.draw_move_repetition_lists[config.list_to_add_move_in_draw_check].append([from_point, to_point])
	
	if len(config.draw_move_repetition_lists[config.list_to_add_move_in_draw_check]) == 2:
		
		if config.list_to_add_move_in_draw_check < 4:
			config.list_to_add_move_in_draw_check += 1
		
		else:
			config.list_to_add_move_in_draw_check = 0


# Returns nothing. Flips the turn.

def flip_turn():
	
	# Try tries to add the index of the turn in the turns and inserts the value into turn.
	
	try:
		config.turn = config.turns[config.turns.index(config.turn) + 1]
	
	# If an IndexError comes it means that the last index of the turns was the turn and had already been played by the player and that the turn must loop back to the 0th index of turns.
	
	except IndexError:
		config.turn = config.turns[0]


# Returns a list with 2 arguments: first one being one of the strings -> "IP" for in progress, "black" if black won, "draw" if the game is a draw and "white" if white won and second one being the reason for the game ending. Checks if game has ended by any player winning or by a draw or it is in progress.

def check_game_end():
	
	# If checks if the all the white or black pieces are eaten, and if they are it returns the other player's side.
	
	if not white_pieces_group:
		return ["black won", "killing all pieces"]
	
	elif not black_pieces_group:
		return ["white won", "killing all pieces"]
	
	# If none of the above statements are true, it checks if the player has played the same move 5 times.
	
	elif config.draw_move_repetition_lists[0] == config.draw_move_repetition_lists[2] == config.draw_move_repetition_lists[4] and config.draw_move_repetition_lists[1] == config.draw_move_repetition_lists[3]:
		return ["draw", "repetition"]
	
	# It lastly checks if the players have played 25 moves without a jump, and if one of this is true, then it returns draw.
	
	elif config.draw_move_count == 50:
		return ["draw", "no jumps for 25 moves"]
	
	return "IP"


# Returns nothing. Makes the animation of white screen rolling from down to below and displays message saying that which side won.

def end_of_game(text, reason):
	
	# Animates the end white screen (moves it upwards from below the screen).
	
	while end_of_game_screen.ycor() < 0:
		
		end_of_game_screen.forward(0.75 * square_len)
		wn.update()
	
	# Lastly it stamps the white screen to allow turtle objects to write on it.
	
	end_of_game_screen.hideturtle()
	end_of_game_screen.clearstamps()
	end_of_game_screen.stamp()
	
	# It writes the text and the reason (for eg: white won = text and by killing all pieces = reason).
	
	end_result_writer.write(f"{text.capitalize()} by {reason.capitalize()}", True, "center", ("Arial", 15, "bold"))


# Returns nothing. Draws pieces on the board.

def draw_pieces():
	
	# For is because there are 32 pieces on the board to be made.
	
	for number_of_loops, index in enumerate(white_screen_coordinates()):
		
		# Point is calculated from index.
		
		point = point_names[index]
		
		# Takes the x and y coords of the points on which the pieces should go.
		
		x_coordinate = point_names[index].x
		y_coordinate = point_names[index].y
		
		# If checks if it is creating the white or the black pieces and creates piece sets the state of that coordinate to the type of itself (white or black) and appends itself to the respective type list (white or black).
		
		if number_of_loops < 16:
			piece = Piece(x_coordinate, y_coordinate, piece_types[0], piece_types[1], number_of_loops, point)
			point_names[index].state = piece_types[0]
			white_pieces_group.append(piece)
		
		else:
			piece = Piece(x_coordinate, y_coordinate, piece_types[1], piece_types[0], number_of_loops, point)
			point_names[index].state = piece_types[1]
			black_pieces_group.append(piece)
		
		# Appends the piece to the pieces_group list.
		
		pieces_group.append(piece)
