#Q4.4.	Write a Python program to get the key, value and item in a dictionary.
#Input: input_dict = {1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60}

# Given Dictionary :-
input_dict= {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}

# dictionary Before removal:-
print("Before removal:")
for k,v in input_dict.items():
    print(f"Key: {k}, Value: {v}, Item: {k,v}")

# Remove items where value is None
input_dict = {k:v for k,v in input_dict.items() if v is not None}

# dictionary after removal:-
print("\nAfter removal of Empty Item:")
for k,v in input_dict.items():
    print(f"Key: {k}, Value: {v}, Item: {k}:{v}")
