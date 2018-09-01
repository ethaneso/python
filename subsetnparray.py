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

# Print out the 5th row of np_baseball
print(np_baseball[4])

# Select the entire second column of np_baseball: np_weight
np_weight = np_baseball[:,1]
print(np_weight)

# Print out height of 7th player
print(np_baseball[6,0])