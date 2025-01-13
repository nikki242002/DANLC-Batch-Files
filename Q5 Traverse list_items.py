#Q5.Write a Python program to traverse a given list in reverse order, and print the elements with the original index.
# Original list: ['red', 'green', 'white', 'black']

original_list = ['red', 'green', 'white', 'black']
length = len(original_list)

for i in range(length -1,-1,-1):
    print(f"Index {i}: {original_list[i]}")
