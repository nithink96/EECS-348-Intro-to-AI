import common

def part_one_classifier(data_train,data_test):
        # PUT YOUR CODE HERE
        # Access the training data using "data_train[i][j]"
        # Training data contains 3 cols per row: X in 
        # index 0, Y in index 1 and Class in index 2
        # Access the test data using "data_test[i][j]"
        # Test data contains 2 cols per row: X in 
        # index 0 and Y in index 1, and a blank space in index 2 
        # to be filled with class
        # The class value could be a 0 or a 1
        w = [0, 0, 0]
        error = 1
        iterations = 1000
        while abs(error) > 0 and iterations > 0:

                error = 0
                for x in range(common.constants.TRAINING_SIZE):
                        activation = w[0] * data_train[x][0] + w[1] * data_train[x][1] + w[2]
                        if activation >= 0:
                                prediction = 1
                        else:
                                prediction = 0

                        actualVal = data_train[x][2]
                        delta = actualVal - prediction
                        w[0] +=  delta * data_train[x][0]
                        w[1] +=  delta * data_train[x][1]
                        w[2] +=  delta
                        error += delta

                iterations -= 1
        for i in range(common.constants.TEST_SIZE):
                if w[0] * data_test[i][0] + w[1] * data_test[i][1] + w[2] >= 0:
                        data_test[i][2] = 1
                else:
                        data_test[i][2] = 0
        return
def part_two_classifier(data_train,data_test):
        # PUT YOUR CODE HERE
        # Access the training data using "data_train[i][j]"
        # Training data contains 3 cols per row: X in 
        # index 0, Y in index 1 and Class in index 2
        # Access the test data using "data_test[i][j]"
        # Test data contains 2 cols per row: X in 
        # index 0 and Y in index 1, and a blank space in index 2 
        # to be filled with class
        # The class value could be a 0 or a 8

        w = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        y = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        learningRate = 0.01
        error = 1
        iterations = 1000

        while abs(error) > 0 and iterations > 0:

                error = 0
                for i in range(common.constants.TRAINING_SIZE):

       			maxVal = -12224
                        for j in range(9):
                                y[j] = w[j][0] * data_train[i][0] + w[j][1] * data_train[i][1] + w[j][2]
                       		if(y[j] > maxVal):
					maxVal = y[j]
					predicted = j
                        actualVal = int(data_train[i][2])
                        delta = predicted - actualVal

                        if predicted != actualVal:
                                w[predicted][0] -= learningRate *  data_train[i][0]
                                w[predicted][1] -= learningRate * data_train[i][1]
                                w[predicted][2] -= learningRate * w[predicted][2] - 1

                                w[actualVal][0] += learningRate * data_train[i][0]
                                w[actualVal][1] += learningRate * data_train[i][1]
                                w[actualVal][2] += learningRate * w[actualVal][2] + 1

                        error += abs(predicted - actualVal)
                iterations -= 1

        for i in range(common.constants.TEST_SIZE):
		maxVal = -23412
                for j in range(9):
                        y[j] = w[j][0] * data_test[i][0] + w[j][1] * data_test[i][1] + w[j][2]
                	if(y[j] > maxVal):
				maxVal = y[j]
				predicted = j
                data_test[i][2] = predicted

        return

