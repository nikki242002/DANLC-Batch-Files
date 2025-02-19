#LAB4.Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
 # Sample Python dictionary data and list labels:
 # exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
 # 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
 # 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
 # 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
 # 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
import pandas as pd
import numpy as np
exam_data = {
    'Name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'Score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'Attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'Qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
df1= df[['Name', 'Score']]
print(df1)
