# Only one dependency: numpy
from numpy import *


def main():
    # Step 1: Import data
    points = genfromtxt('Data/grade_points.csv', delimiter=',')
    print(points)


if __name__ == '__main__':
    main()
