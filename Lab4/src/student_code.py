import common

class variables:
	counter=0

def sudoku_backtracking(sudoku):
	# PUT YOUR CODE HERE
	# access the sudoku using "sudoku[y][x]"
	# y between 0 and 9
	# x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 
	variables.counter=0
	emptySpaces = findEmpty(sudoku)
	recursionBacktracking(sudoku, emptySpaces)
	return variables.counter
def recursionBacktracking(sudoku, emptySpaces):
	variables.counter +=1
	if (not emptySpaces):
		return True
	i,j = emptySpaces.pop(0)
	for k in range(1, 10):
		#variables.counter += 1
		if(nineWay_AllDiff(sudoku, i, j, k)):
			sudoku[i][j] = k
			result = recursionBacktracking(sudoku, emptySpaces)
			if result == True:
				return result
			sudoku[i][j] = 0
	emptySpaces.insert(0, (i,j))
	return False

def findEmpty(sudoku):
	emptySpaces = []
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				emptySpaces.append((i,j))
	return emptySpaces
def nineWay_AllDiff(sudoku, y, x, val):
	for i in range(9):
		if (sudoku[y][i] == val):
			return False
		if (sudoku[i][x] == val):
			return False
		if(sudoku[(y/3)*3+i/3][(x/3)*3+i%3] == val):
			return False
	return True		
def sudoku_forwardchecking(sudoku):
	# PUT YOUR CODE HERE
        # access the sudoku using "sudoku[y][x]"
        # y between 0 and 9
        # x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 
	variables.counter = 0
	emptySpaces = findEmpty(sudoku)
	values = findDomain(sudoku)
	recursionForwardchecking(sudoku, values, emptySpaces)
	return variables.counter

def recursionForwardchecking(sudoku, values, emptySpaces):
	variables.counter += 1
	if not emptySpaces:
		return True
	current = emptySpaces.pop(0)
	i, j = current
	currentDomain = values[current]
	values.pop(current)

	for val in currentDomain:
		sudoku[i][j] = val
		copyValues = copyDict(values)
		if not removeIncorrectValues(sudoku, copyValues):
			result = recursionForwardchecking(sudoku, copyValues, emptySpaces)
			if result == True:
				return result
		sudoku[i][j] = 0
	emptySpaces.insert(0, current)
	values[current] = currentDomain
	return False

def removeIncorrectValues(sudoku, values):
	removed = False
	for var, val in values.iteritems():
		i, j = var
		for k in values[var]:
			if not nineWay_AllDiff(sudoku, i, j, k):
				values[var].remove(k)
			if not values[var]:
				removed = True
	return removed

def findDomain(sudoku):
	domain = {}
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				domain[(i,j)] = []
	for var, val in domain.iteritems():
		i,j = var
		for k in range(1,10):
			if nineWay_AllDiff(sudoku, i, j, k):
				val.append(k)
	return domain

def sudoku_mrv(sudoku):
	# PUT YOUR CODE HERE
        # access the sudoku using "sudoku[y][x]"
        # y between 0 and 9
        # x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 
	variables.counter = 0
	values = findDomain(sudoku)
	emptySpaces = findEmpty(sudoku)
	recursionMRV(sudoku, values, emptySpaces)
	return variables.counter

def recursionMRV(sudoku, values, emptySpaces):
	variables.counter += 1
	emptySpaces = sorted(values, key=lambda k: len(values[k]), reverse = False)
	if not emptySpaces:
		return True

        current = emptySpaces.pop(0)
        i, j = current
        currentDomain = values[current]
        values.pop(current)

        for val in currentDomain:
                sudoku[i][j] = val
        #	variables.counter += 1
	        copyValues = copyDict(values)
                if not removeIncorrectValues(sudoku, copyValues):
                        result = recursionMRV(sudoku, copyValues, emptySpaces)
                        if result == True:
                                return result
                sudoku[i][j] = 0
        emptySpaces.insert(0, current)
        values[current] = currentDomain
        return False

def copyDict(dictionary):
	newDict =  {}
	for key in dictionary:
		newDict[key] = []
	for key, values in dictionary.iteritems():
		for val in values:
			newDict[key].append(val)
	return newDict
