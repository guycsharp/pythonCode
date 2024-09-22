import os
import json
from deepdiff import DeepDiff

path1 = 'C:/pythonCode/JsonCompare/testFile/Json/'
path2 = 'C:/pythonCode/JsonCompare/testFile/Json/'


print(f'{path1} vs {path2}')
# get the list of json files in both directories
folder1_files1 = [f for f in os.listdir(path1) if f.endswith('.json')]
folder2_files2 = [f for f in os.listdir(path2) if f.endswith('.json')]

count = 0

# assuming both folders have same json files
for file in folder1_files1:
    if file in folder2_files2:
        with open(f'{path1}{file}') as file_1, open(f'{path2}{file}') as file_2:
            data_1 = json.load(file_1)
            data_2 = json.load(file_2)

        differences = DeepDiff(data_1, data_2, ignore_order=True)
        count = count + 1

        if differences:
            print(f'Differences between files in {file}:')
            print(differences)
        # else:
        #     print(f'Files {file} in both folders are the same.')

    else:
        print(f"File {file} doesn't exist in folder2")

print(count)