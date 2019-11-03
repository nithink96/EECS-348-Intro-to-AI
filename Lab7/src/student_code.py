import common
import math

def detect_slope_intercept(image):
        # PUT YOUR CODE HERE
        # access the image using "image[chanel][y][x]"
        # where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
        # set line.m and line.b
        # to create an auxiliar bidimentional structure 
        # you can use "space=common.init_space(heigh, width)"
        line=common.Line()
        hough_space = common.init_space(2000, 2000)
        for y in range(common.constants.HEIGHT):
                for x in range(common.constants.WIDTH):
                        if ((image[0][y][x] == 0) and (image[1][y][x] == 0) and (image[2][y][x] == 0)):
                                for m_space in range(0, 2000):
                                        m = float(m_space) / float(100) - 10
                                        b = -(m * x) + y
                                        if (b > -1000 and b < 1000):
                                                hough_space[m_space][int(b) + 1000] += 1
        maximum = -1
        for y in range(2000):
                for x in range(2000):
                        if hough_space[y][x] > maximum:
                                maximum = hough_space[y][x]
                                m = float(y) / 100 - 10
                                b = x - 1000.4
        line.m = m
        line.b = b

        return line

def detect_normal(image):
        # PUT YOUR CODE HERE
        # access the image using "image[chanel][y][x]"
        # where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
        # set line.theta and line.r
        # to create an auxiliar bidimentional structure 
        # you can use "space=common.init_spa
        line=common.Line()
        hough_space = common.init_space(1800, 1800)
        for y in range(common.constants.HEIGHT):
                for x in range (common.constants.WIDTH):
                        if ((image[0][y][x] == 0) and (image[1][y][x] == 0) and (image[2][y][x] == 0)):
                                for theta_space in range(0, 1800):
                                        theta = math.radians(float(theta_space) / float(10))
                                        r = x * math.cos(theta) - y * math.sin(theta)
                                        if (r > -900 and r < 900):
                                                hough_space[theta_space][int(r) + 900] += 1
        maximum = -1
        for y in range(1800):
                for x in range(1800):
                        if hough_space[y][x] > maximum:
                                maximum = hough_space[y][x]
                                theta = math.pi - math.radians(float(y) / float(10))
                                r = 900 - x
        line.r = r
        line.theta = theta

        return line
def detect_circles(image):
	# PUT YOUR CODE HERE
	# access the image using "image[chanel][y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	hough_space = common.init_space(common.constants.HEIGHT, common.constants.WIDTH)
	numCircles = 0
	image = image[0]
	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			if( y > 0 and y< common.constants.HEIGHT - 1 and x > 0 and x < common.constants.WIDTH - 1):
				if image[y][x] == 0:
					if( image[y+1][x] == 255 or image[y-1][x] == 255 or image[y][x+1] or image[y][x-1]):
						for b in range(common.constants.HEIGHT):
							for a in range(common.constants.WIDTH):
								if( round((x-a)**2 + (y-b)**2) == 900):
									hough_space[int(b)][a] += 1 

	for y in range(480):
		for x in range(640):
			if hough_space[y][x] > 10:
				numCircles += 1

	return numCircles
