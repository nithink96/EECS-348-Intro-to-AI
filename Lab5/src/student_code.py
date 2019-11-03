import common

def drone_flight_planner (map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle):
	discount_per_cycle = 1 - discount_per_cycle
	actions = [1, 2, 3, 4, 5, 6, 7, 8]
	states = [1, 2, 3, 4]
	for i in range(6):
		for j in range(6):
			if map[i][j] == 3 :
				values[i][j] = -dronerepair_cost
				policies[i][j] = 0
			if map[i][j] == 2:
				values[i][j] = delivery_fee
				policies[i][j] = 0
	while True:
		oldValues = [row[:] for row in values]
		oldPolicies = [row[:] for row in policies]
		for i in range(6):
			for j in range(6):
				maxValue = -float('-inf')
				if map[i][j] != 3 and map[i][j] != 2:	
					for action in actions:
						value = 0
						for state in states:
							if state == 1:
								newI = i
								newJ = j + 1
							elif state == 2:
								newI = i - 1
								newJ = j
							elif state == 3:
								newI = i
								newJ = j - 1
							elif state == 4:
								newI = i + 1
								newJ = j
							T = transition(newI, newJ, i, j, action)
							R = reward(action, battery_drop_cost)
							if not (newI < 0 or newI > 5 or newJ < 0 or newJ > 5):
								value += T * (R + discount_per_cycle * oldValues[newI][newJ])
							else:
								if newI < 0:
									value += T * (R + discount_per_cycle * oldValues[i][newJ])
								if newI > 5:
									value += T * (R + discount_per_cycle * oldValues[i][newJ])
								if newJ < 0:
									value += T * (R + discount_per_cycle * oldValues[newI][j])
								if newJ > 5:
									value += T * (R + discount_per_cycle * oldValues[newI][j])	
						if value > maxValue:
							maxValue = value
							policies[i][j] = action
							values[i][j] = maxValue
		if checkValues(values, oldValues) and checkPolicies(policies , oldPolicies):
			break
	return startVal(map, values)

def reward(action, battery_drop_cost):
	if action == 1 or action == 2 or action == 3 or action == 4:
		return -battery_drop_cost
	if action == 5 or action == 6 or action == 7 or action == 8:
		return -(2 * battery_drop_cost)

def transition(newI, newJ, i, j, action):
	if action == 1:
		if newI == i + 1:
			return 0.7
		if newJ == j + 1 or newJ == j - 1:
			return 0.15
	if action == 2:
		if newJ == j - 1:
			return 0.7
		if newI == i + 1 or newI == i - 1:
			return 0.15
	if action == 3:
		if newI == i - 1:
			return 0.7
		if newJ == j + 1 or newJ == j - 1:
			return 0.15
	if action == 4:
		if newJ == j + 1:
			return 0.7
		if newI == i + 1 or newI == i - 1:
			return 0.15
	if action == 5:
		if newI == i + 1:
			return 0.8
		if newJ == j + 1 or newJ == j - 1:
			return 0.1
	if action == 6:
		if newJ == j - 1:
			return 0.8
		if newI == i + 1 or newI == i - 1:
			return 0.1
	if action == 7:
		if newI == i - 1:
			return 0.8
		if newJ == j + 1 or newJ == j - 1:
			return 0.1
	if action == 8:
		if newJ == j + 1:
			return 0.8
		if newI == i + 1 or newI == i - 1:
			return 0.1
	return 0.0

def checkValues(values, oldValues):
	for i in range(6):
		for j in range(6):
			if abs(values[i][j] - oldValues[i][j]) > 0.01 : 
				return False
	return True

def checkPolicies(policies, oldPolicies):
	for i in range(6):
		for j in range(6):
			if policies[i][j] != oldPolicies[i][j]:
				return False
	return True

def startVal(map, values):
	for i in range(6):
		for j in range(6):
			if map[i][j] == 1:
				return values[i][j]

