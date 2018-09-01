# variable: place
place = " poolhouse "

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place, place_up)

# returns the lowercase version of place_up
print(place_up.lower())

# returns a string with whitespace removed from the start and end
print(place.strip())

# tests if all the string characters are alphabets
print(place.isalpha())

# tests if the string characters are digits
print(place.isdigit())

# tests if the string characters are whitespace characters
print(place.isspace())

# searchs for "l" within the string
print(place.find('l'))

# returns a string where all occurrences of replaced by 
print(place.replace('l', 'r'))

# separated by 'h'
print(place.split('h'))

# Converts first character to Capital letter
print(place.capitalize())

# Converts to casefolded strings
print(place.endswith('e'))
