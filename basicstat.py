# list of lists
baseball = [[1.79, 130],
			[1.80, 125],
			[1.88, 140],
			[1.99, 150],
			[2.00, 150],
			[1.84, 134],
			[1.77, 125],
			[1.84, 127]]

# Import numpy
import numpy as np

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the mean of height
np_height = np_baseball[:,0]
print(np.mean(np_height))

# Print out the median of height
print(np.median(np_height))