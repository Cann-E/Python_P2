# Sample list of numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing examples
print("Full list:", numbers[:])        # Get the entire list
print("First 5 elements:", numbers[:5])  # Get first 5 elements
print("Last 3 elements:", numbers[-3:])  # Get the last 3 elements
print("Middle slice (index 2 to 6):", numbers[2:7])  # Get elements from index 2 to 6
print("Every second element:", numbers[::2])  # Get every second element
print("Reverse list:", numbers[::-1])  # Reverse the list

# String slicing example
text = "Hello, World!"
print("First 5 characters:", text[:5])  # Get first 5 characters
print("Last 6 characters:", text[-6:])  # Get last 6 characters
print("Reverse text:", text[::-1])  # Reverse the string



# list[start:stop:step]
# start → Where slicing begins (default 0 if omitted).
# stop → Where slicing stops (excludes this index).
# step → The step size (default 1).
