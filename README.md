# Gradient Descent Applied to Linear Regression

This is a basic implementation of linear regression and gradient descent which, in this case, models time spent studying and grade scores for 100 students.

Using gradient descent, we can find the optimal line defined simply by 'y = mx + b' which best fits a linear data set. The gradient descent algorithm iterates several possible line fits, each time calculating the total error.  Finding the [partial derivatives](https://spin.atomicobject.com/wp-content/uploads/linear_regression_gradient1.png) for both the y-intercept and slope, it can decide which direction to test in the next iteration of some m and b. The user, in this case, must feed an initial guess for the slope, y-intercept, learning rate, and total number of iterations.

Determining the best learning rate is an optimzation problem in and of itself.  This conundrum actually represents a more general struggle of fine-tuning so-called hyper-parameters in machine learning.  Maybe we can use machine learning to optimize a machine learning solution (ML-ception)!