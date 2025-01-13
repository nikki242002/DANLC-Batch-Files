#Q1.Write a Python program and calculate the mean of the below dictionary.
# test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}

test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
total = sum(test_dict.values())
count = len(test_dict)
mean = total / count
print(f" The mean of the dictionary values is: {mean}")

