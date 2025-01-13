# Q3.Write a Python program to find duplicate values from a list and display those.
numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1]
duplicates = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j] and numbers[i] not in duplicates:
            duplicates.append(numbers[i])

print("Duplicate values in the list are:", duplicates)
