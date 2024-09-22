
import json
from deepdiff import DeepDiff

# Open and load the second JSON file

file1 = ''
file2 = ''

with open(file1) as file_1, open(file2) as file_2:
    data_1 = json.load(file_1)
    data_2 = json.load(file_2)

differences = DeepDiff(data_1, data_2,   ignore_order=True)

if differences:
    print('Differences between files:')
    print(differences)
else:
    print('Files are the same.')