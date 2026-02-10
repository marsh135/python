import random  # Import Python's built-in random module

# Create an empty list to store random numbers
randomNums = []

# Generate 10 random integers between 1 and 100 and add them to the list
for i in range(10):
    num1 = random.randint(1, 100)  # Generate a random integer
    randomNums.append(num1)        # Add it to the list

# Display the generated list and various operations on it
print(randomNums)  # The full list of random numbers

print("The largest number is:", max(randomNums))        # Maximum number
print("The smallest number is:", min(randomNums))       # Minimum number
print("The sum of all numbers is:", sum(randomNums))    # Sum of all numbers
print("The average of the numbers is:", sum(randomNums) / len(randomNums))  # Average

print("The sorted list is:", sorted(randomNums))                     # Sorted ascending
print("The list in reverse order is:", list(reversed(randomNums)))   # Reverse order
print("The list without duplicates is:", list(set(randomNums)))      # Unique values only

print("The first five numbers are:", randomNums[:5])   # Slice: first 5
print("The last five numbers are:", randomNums[-5:])   # Slice: last 5

print("The numbers at even indices are:", randomNums[::2])  # Elements at even indices
print("The numbers at odd indices are:", randomNums[1::2])  # Elements at odd indices

# Sample dictionary for demonstration
sampleDict = {
    'a': 1, 
    'b': 2, 
    'c': 3, 
    'd': 4,
    'e': 5
}

# Display dictionary data and operations
print("The keys of the dictionary are:", list(sampleDict.keys()))      # All keys
print("The values of the dictionary are:", list(sampleDict.values()))  # All values
print("The items of the dictionary are:", list(sampleDict.items()))    # Key-value pairs
print("The dictionary sorted by keys is:", dict(sorted(sampleDict.items())))  # Sorted by keys

# Loop through dictionary and print key-value pairs
for key in sampleDict:
    print(f"Key: {key}, Value: {sampleDict[key]}")

# Access a specific value by key
print(sampleDict['a'])  # Prints the value associated with key 'a'