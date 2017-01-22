# Only one dependency: numpy
from numpy import *


def compute_error(b, m, points):
    # Calculate distance of a given point to the line
    total_error = 0 # Initialize error at zero

    # For every data point in our set, compute the error
    for i in range(0, len(points)):
    	x = points[i, 0] # x value at position i
    	y = points[i, 1] # y value at position i
    	total_error += (y - (m * x + b)) ** 2 # Summation of squared distances

    # Return the average, total error of each point
    return total_error / float(len(points))


def step_gradient(b_current, m_current, points, learning_rate):
	# Step Gradient function
	b_gradient = 0
	m_gradient = 0
	N = float(len(points))

	for i in range(0, len(points)):
		x = points[i, 0]
		y = points[i, 1]

		# Direction with respect to b and m
		# Calculate partial derivative of each error at a given point
		b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
		m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))

	# Update b and m values using the partial derivatives
	new_b = b_current - (learning_rate * b_gradient)
	new_m = m_current - (learning_rate * m_gradient)

	# Return each b and m for every iteration
	return [new_b, new_m] 


def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
	# Starting y-intercept, b and slope, m
	b = starting_b
	m = starting_m

	# Perform Gradient Descent
	for i in range(num_iterations):
		# Update b and m with more accurate version with each gradient step
		b, m = step_gradient(b, m, array(points), learning_rate)
	return [b, m]


def main(learning_rate, initial_b, initial_m, iterations):
	# Step 1: Import data
	points = genfromtxt('Data/grade_points.csv', delimiter=',')
	
	# Step 2: Define Hyperparameters of the model
	learning_rate = learning_rate # How Fast should the model learn?
	initial_b = initial_b # Begin with a y-intercept of 0 
	initial_m = initial_m # Begin with a slope of 0
	num_iterations = iterations # Perform 1000 iterations

	# Step 3: Train the model
	print('Gradient Descent begins at b = {0}, m = {1}, and error = {2}'.format(initial_b, initial_m, compute_error(initial_b, initial_m, points)))
	[b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
	print('After {0} iterations: b = {1}, m = {2}, error = {3}'.format(num_iterations, b, m, compute_error(b, m, points)))


if __name__ == '__main__':
    main(0.000005, 0, 0, 200)
