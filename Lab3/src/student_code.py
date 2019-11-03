import common

def minmax_tictactoe(board, turn):
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);
	result = common.game_status(board)
	#common.print_board(board)
#	print("\n")
	if result == common.constants.O or result == common.constants.X:
		return result
	if result == common.constants.NONE and isFull(board) == 1:
		return result
	if turn == common.constants.X:
		return max_val(board)
	if turn == common.constants.O:
		return min_val(board)
def max_val(board):
        v = common.constants.O
        for i in range(0,3):
                for j in range(0,3):
                        if common.get_cell(board, i, j) == common.constants.NONE:
                                common.set_cell(board,i,j,common.constants.X)
                      		v = max(v, minmax_tictactoe(board, common.constants.O))
				common.set_cell(board, i, j, common.constants.NONE)
        return v


def min_val(board):
        v = common.constants.X
        for i in range(0,3):
                for j in range(0,3):
                        if common.get_cell(board, i, j) == common.constants.NONE:
                                common.set_cell(board, i, j, common.constants.O)
                      		v = min(v, minmax_tictactoe(board, common.constants.X))
				common.set_cell(board, i, j, common.constants.NONE)
        return v

def abprun_tictactoe(board, turn):
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);
	return abprun_tictactoe_helper(board, turn, common.constants.O, common.constants.X)
def abprun_tictactoe_helper(board, turn, alpha, beta):
	result = common.game_status(board)	
	#common.print_board(board)
	#print("\n")
	if result == common.constants.O or result == common.constants.X:
		return result
	if result == common.constants.NONE and isFull(board) == 1:
		return result
	if turn == common.constants.X:
		return max_val_ABPrun(board, alpha, beta)
	if turn == common.constants.O:
		return min_val_ABPrun(board, alpha, beta)
def max_val_ABPrun(board, alpha, beta):
	v = common.constants.O
	for i in range(0,3):
		for j in range(0,3):
			if common.get_cell(board, i, j) == common.constants.NONE:
				common.set_cell(board,i,j,common.constants.X)
				v = max(v, abprun_tictactoe_helper(board, common.constants.O, alpha, beta))
				common.set_cell(board, i, j, common.constants.NONE)	
				if v == max(v, beta):
					return v
				alpha = max(alpha, v)
	return v


def min_val_ABPrun(board, alpha, beta):
	v = common.constants.X
	for i in range(0,3):
		for j in range(0,3):
			if common.get_cell(board, i, j) == common.constants.NONE:
				common.set_cell(board, i, j, common.constants.O)
				v = min(v, abprun_tictactoe_helper(board, common.constants.X, alpha, beta))
              		 	common.set_cell(board, i, j, common.constants.NONE)
				if v == min(v, alpha):
                       		 	return v
               			beta = min(beta, v)
        return v
def max(v,min_max):
	if v == common.constants.X or min_max == common.constants.X:
		return common.constants.X
	if v ==common.constants.NONE or min_max == common.constants.NONE:
		return common.constants.NONE
	
	return common.constants.O 
def min(v, min_max):
        if v == common.constants.O or min_max == common.constants.O:
                return common.constants.O
        if v == common.constants.NONE or min_max == common.constants.NONE:
                return common.constants.NONE
        
        return common.constants.X


def isFull(board):
	for i in range(0,3):
		for j in range(0,3):
			if common.get_cell(board,i, j) == common.constants.NONE:
				return False
	return True	
