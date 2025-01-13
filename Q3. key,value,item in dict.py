#Q3.Write a Python program to get the key, value and item in a dictionary.
#input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# given Dictionary:-
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

for k,v in dict_num.items():
    print(f"Key: {k}, Value: {v}, Item: {k,v}")
