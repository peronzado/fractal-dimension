import numpy as np

def box_counting(points, box_size):
    # Calculate the number of boxes in each direction
    num_boxes = np.ceil((np.max(points, axis=0) - np.min(points, axis=0)) / box_size).astype(int)

    # Initialize the box count array
    box_count = np.zeros(num_boxes)

    # Iterate over all points and count the number of points in each box
    for i in range(points.shape[0]):
        box = np.floor((points[i] - np.min(points, axis=0)) / box_size).astype(int)
        box_count[box[0], box[1]] += 1

    # Count the number of non-empty boxes
    return np.sum(box_count > 0)

def fractal_dimension(points):
    # List of box sizes
    num_boxes = 100
    max_box_size = 0.05
    box_sizes = np.logspace(-2, np.log10(max_box_size), num=num_boxes, endpoint=True)

    # List of box counts
    box_counts = np.zeros(len(box_sizes))

    # Loop over box sizes
    for i, size in enumerate(box_sizes):
        box_counts[i] = box_counting(points, size)

    # Linear regression to find the fractal dimension
    slope, _ = np.polyfit(np.log(box_sizes), np.log(box_counts), 1)

    return slope

# Get the number of points from the user
num_points = int(input("Enter the number of points: "))

# Generate random points in 2D
points = np.random.rand(num_points, 2)

# Calculate the fractal dimension of the points
dimension = fractal_dimension(points)
