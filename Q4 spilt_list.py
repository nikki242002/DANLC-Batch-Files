#Q4.Write a Python program to split a given list into two parts where the length of the first part of the list is given.
original_list = ['apple', 1, 2, 3, 'mango', 4, 'orange', 1]

length_of_first_part = 3

first_part = original_list[:length_of_first_part]
second_part = original_list[length_of_first_part:]

print("Splitted the said list into two parts:", (first_part, second_part))
