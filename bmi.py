# height as in inches
height = [74, 72, 69, 71, 73, 69, 70, 79, 72, 76, 75, 71]

# weights as in pounds
weight = [180, 215, 188, 176, 180, 160, 210, 176, 209, 219, 199, 205]

# Import numpy
import numpy as np

# Create a numpy array from height: np_height
np_height = np.array(height)

# Create a numpy array from weight: np_weight
np_weight = np.array(weight)

# Print out np_height, np_weight
print(np_height, np_weight)

# Convert np_height from inches to meters: np_height_m
np_height_m = np_height * 0.0254

# Convert np_weight from pounds to kg
np_weight_kg = np_weight * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg/np_height_m**2

# Print out bmi
print(bmi)
