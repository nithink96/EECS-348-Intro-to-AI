import common
def astar_search(map):
	found = False
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	start = (0,0)
	end = (0,0)
    	for i in range(0, common.constants.MAP_HEIGHT):
        	for j in range(0, common.constants.MAP_WIDTH):
        	    if(map[i][j] == 2):
                	start = (i,j)
        	    if(map[i][j] == 3):
   	           	end = (i,j)
		#	print(end,start)
	Queue = AstarQueue()
	distFromStart = {}
    	parent = {}
    	parent[start] = None
    	f_initial = manhattan_distance(start, end)
	distFromStart[start] = 0
    	start_y, start_x = start
	current = start
	Queue.push(f_initial, start)
    	while(Queue.length() > 0):
        	y,x = Queue.pop()
       		if map[y][x] == 3:
			map[y][x] = 5
			while(parent[current] != None):
				y,x = current
				map[y][x] = 5
				current = parent[current]
			map[start_y][start_x] = 5
			found =  True
			break
		else:
        	 	map[y][x] = 4
		 	if(y >= 0 and y <common.constants.MAP_HEIGHT and x+1 >= 0 and x+1 < common.constants.MAP_WIDTH and (map[y][x+1] == 0 or map[y][x+1] == 3)):
				current = (y,x+1)
				distFromStart[current] = distFromStart[(y, x)] + 1
				f1 = distFromStart[current] + manhattan_distance(current, end)
				Queue.push(f1, current)
				parent[current] = (y, x)
				
			
			if(y >= 0 and y+1 < common.constants.MAP_HEIGHT and x >= 0 and x < common.constants.MAP_WIDTH and (map[y+1][x] == 0 or map[y+1][x] == 3)):
				current = (y+1,x)
				distFromStart[current] = distFromStart[(y, x)] + 1
				f2 = distFromStart[current] + manhattan_distance(current, end)
				Queue.push(f2,current)
				parent[current] = (y, x)
			
			
			if(y >= 0 and y < common.constants.MAP_HEIGHT and x-1 >= 0 and x-1 < common.constants.MAP_WIDTH and (map[y][x-1] == 0 or map[y][x-1] == 3)):
				current = (y,x-1)
				distFromStart[current] = distFromStart[(y, x)] + 1
				f3 = distFromStart[current] + manhattan_distance(current, end)
				Queue.push(f3,current)
				parent[current] = (y, x)
				
			if(y-1 >= 0 and y-1 < common.constants.MAP_HEIGHT and x >= 0 and x < common.constants.MAP_WIDTH and (map[y-1][x] == 0 or map[y-1][x] == 3)):
				current = (y-1,x)
				distFromStart[current] = distFromStart[(y, x)] + 1
				f4 = distFromStart[current] + manhattan_distance(current, end)
				Queue.push(f4,current)
				parent[current] = (y, x)

	return found

def manhattan_distance(start, end):
	y_start, x_start = start
	y_end, x_end = end
	a = (abs(y_start - y_end) + abs(x_start - x_end))
	return(a)
class AstarQueue(object):
	def __init__(self):
		self.Queue = []
	
	def push(self, new_f, new_point):
		new_y, new_x = new_point
		i = 0
		if not self.Queue:
			self.Queue.append((new_f, new_point))
			return
		else:
			for f, point in self.Queue:
				y, x = point

				if f > new_f:
					i += 1
					
					
				elif f == new_f:

					if x < new_x:
						self.Queue.insert(i, (new_f, new_point))	
						return
					elif x == new_x:

						if y < new_y:
							self.Queue.insert(i, (new_f, new_point))
							return
					else:
						i += 1
					
					

				else: 
					self.Queue.insert(i, (new_f, new_point))
					return
			i += 1
			self.Queue.append((new_f, new_point))
	def length(self):
		return(len(self.Queue))
	def pop(self):
		f, point = self.Queue.pop()
		return point

