# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_2 = [2.4, 3.3, 2.9, 4.2, 5.8]

# sorts the list
areas.sort()
print(areas)

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# inserts element at the given index
areas.insert(2, 21.0)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# adds the elements in another list to the ned of the list
areas.extend(areas_2)

# Print out areas
print(areas)

# Searches for the given element and returns its index
print(areas.index(5.8))

# Searches for the first instance of the given element and removes it
areas.remove(11.25)
print(areas)

