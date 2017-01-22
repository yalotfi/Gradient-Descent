# Only one dependency: numpy
from numpy import *

'''
# Trying to abstract the data to be modeled for more use cases
def load_csv(csv_lib_path):
	# Provide path to your data source
	data = genfromtxt(csv_lib_path, delimiter=',')
	return data
'''


def compute_error(m, b, data):
    # Calculate distance of a given point to the line
    total_error = 0 # Initialize error at zero

    # For every data point in our set, compute the error
    for i in range(0,len(points)):
    	x = points[i, 0] # x value at position i
    	y = points[i, 1] # y value at position i
    	total_error += (y - (m * x + b)) ** 2 # Summation of squared values

    # Return the average, total error of each point
    return total_error / float(len(points))


def step_gradient(b_current, m_current, points, learning_rate):
	# Step Gradient function
	return 0


def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
	# Running gradient descent function
	return 0


def main():
	# Step 1: Import data
	points = genfromtxt('Data/grade_points.csv', delimiter=',')
	
	# Step 2: Define Hyperparameters of the model
	learning_rate = 0.0001 # How Fast should the model learn?
	initial_b = 0 # Begin with a y-intercept of 0 
	initial_m = 0 # Begin with a slope of 0
	num_iterations = 1000 # Perform 1000 iterations

	# Step 3: Train the model
	print('Gradient Descent begins at b = {0}, m = {1}, and error = {2}'.format(initial_b, initial_m, compute_error(b, m, points)))
	[b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
	print('After {0} iterations: b = {1}, m = {2}, error = {3}'.format(num_iterations, b, m, compute_error(b, m, pointss)))


if __name__ == '__main__':
    main()
