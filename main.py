import numpy as np
import matplotlib.pyplot as plt

print("Welcome to SVM Engenharia's fractal number analysis, designed by Victor Peron.\n")

num_dimensions = int(input("Enter the number of dimensions in which you would like to randomly distribute points (1, 2, or 3): "))
#num_points = int(input("Enter the number of points to generate: "))

if num_dimensions == 1:

    from D import fractal_dimension
    from D import num_points

    points = np.random.rand(num_points)
    plt.plot(points, np.zeros_like(points), '.', color='black')
    plt.title("1D Random Points")
    plt.show()

    dimension = abs(fractal_dimension(points))
    print(f"The fractal dimension of the points in 1D is: {dimension}")

elif num_dimensions == 2:
    from DD import fractal_dimension
    from DD import num_points

    points = np.random.rand(num_points, 2)

    plt.plot(points[:, 0], points[:, 1], '.', color='black')
    plt.title("2D Random Points")
    plt.show()

    dimension = abs(fractal_dimension(points))
    print(f"The fractal dimension of the points in 2D is: {dimension}")

elif num_dimensions == 3:
    from DDD import fractal_dimension
    from DDD import num_points

    points = np.random.rand(num_points, 3)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], '.', color='black')
    ax.set_title("3D Random Points")
    plt.show()

    dimension = abs(fractal_dimension(points))
    print(f"The fractal dimension of the points in 3D is: {dimension}")

else:
    print("Invalid number of dimensions.")
