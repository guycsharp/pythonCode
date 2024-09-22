import pandas as pd
print(pd.__file__)

path1 = 'C:/pythonCode/JsonCompare/testFile/excel/'
path2 = 'C:/pythonCode/JsonCompare/testFile/excel/'

file1 = 'Inventory list with highlighting1.xlsx'
file2 = 'Inventory list with highlighting2.xlsx'

# Load spreadsheets
dataframe1 = pd.read_excel(path1 + file1)
dataframe2 = pd.read_excel(path2 + file2)

# Compare the two DataFrames
difference = dataframe1.compare(dataframe2)

# Print rows with differences, if any
if not difference.empty:
    print(difference)
else:
    print("DataFrames are entirely identical.")