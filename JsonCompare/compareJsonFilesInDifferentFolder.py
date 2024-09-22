import os
import json
from deepdiff import DeepDiff


def count_deep_records(data):
    if isinstance(data, dict):
        return sum(count_deep_records(v) for v in data.values())
    elif isinstance(data, list):
        return sum(count_deep_records(v) for v in data)
    else:
        return 1


def sum_counts(data):
    total = 0
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'count':
                total += value
            elif key == 'computed':
                # parse string into json and recursively process it
                total += sum_counts(json.loads(value))
            else:
                total += sum_counts(value)
    elif isinstance(data, list):
        for item in data:
            total += sum_counts(item)
    return total


folder1 = 'C:/pythonCode/JsonCompare/testFile/Json/'
folder2 = 'C:/pythonCode/JsonCompare/testFile/Json/'


folder1_files = [f for f in os.listdir(folder1) if f.endswith('.json')]
folder2_files = [f for f in os.listdir(folder2) if f.endswith('.json')]

same_files = 0
different_files = 0
total_records_1 = 0
total_records_2 = 0
total_counts_1 = 0
total_counts_2 = 0


count_diff_file_names = ''


for file in folder1_files:
    total_records_file1 = 0
    total_records_file2 = 0
    total_counts_file1 = 0
    total_counts_file2 = 0
    if file in folder2_files:
        with open(f'{folder1}{file}') as file_1, open(f'{folder2}{file}') as file_2:
            data_1 = json.load(file_1)
            data_2 = json.load(file_2)
            total_records_file1 += count_deep_records(data_1)
            total_records_file2 += count_deep_records(data_2)
            total_records_1 += count_deep_records(data_1)
            total_records_2 += count_deep_records(data_2)
            total_counts_file1 += sum_counts(data_1)
            total_counts_file2 += sum_counts(data_2)
            total_counts_1 += sum_counts(data_1)
            total_counts_2 += sum_counts(data_2)

        differences = DeepDiff(data_1, data_2, ignore_order=True)

        if differences:
            # print(f'Differences between files in {file}:')
            # print(differences)
            different_files += 1
            diff_values = differences.get('values_changed')
            if diff_values:
                for keypath in diff_values.keys():
                    keypath_parts = keypath.split('[')[1:-1]
                    dict_path = []
                    for part in keypath_parts:
                        dict_path.append(part.replace(']', '').replace("'", ''))

                    temp_dict1 = data_1
                    temp_dict2 = data_2
                    for key in dict_path:
                        try:
                            key = int(key)
                        except ValueError:
                            pass
                        temp_dict1 = temp_dict1[key]
                        temp_dict2 = temp_dict2[key]
                    print(temp_dict1)
                    print(temp_dict2)
                    print(f'Differences between files in {file}:')
        else:
            print(f'Files {file} in both folders are the same.')
            same_files += 1
        print(f'Total deep records in file 1: {total_records_file1}')
        print(f'Total deep records in file 2: {total_records_file2}')
        print(f'Total deep records count in file 1: {total_counts_file1}')
        print(f'Total deep records count in file 2: {total_counts_file2}')

        if total_records_file1 != 0:
            percentage_difference = abs((total_records_file1 - total_records_file2) / total_records_file1) * 100
            print(f'Percentage difference between total  records in file 1 and 2: {percentage_difference}%')

        if total_records_file1 != total_records_file2:
            # count_diff_file_names += file_1 ','
            print(f"{file_1} is not consistent")
    else:
        print(f"File {file} doesn't exist in folder2")

print(f'\nSummary:')
print(f'Number of the same files: {same_files}')
print(f'Number of different files: {different_files}')
print(f'Total deep records in directory 1: {total_records_1}')
print(f'Total deep records in directory 2: {total_records_2}')
print(f'Total count in folder1: {total_counts_1}')
print(f'Total count in folder2: {total_counts_2}')


if total_records_1 != 0:
    percentage_difference = abs((total_records_1 - total_records_2) / total_records_1) * 100
    print(f'Percentage difference between total deep records in directory 1 and 2: {percentage_difference}%')
else:
    print("Total records in directory 1 is 0, so can't find percentage difference.")