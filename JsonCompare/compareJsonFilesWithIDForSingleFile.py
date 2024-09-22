import os
import json
import collections
from deepdiff import DeepDiff


def get_deep_records_by_report_id(data, records=None):
    if records is None:
        records = collections.defaultdict(list)

    if isinstance(data, dict):
        if "reportId" in data:
            records[data["reportId"]].append(data)
        for v in data.values():
            get_deep_records_by_report_id(v, records)
    elif isinstance(data, list):
        for v in data:
            get_deep_records_by_report_id(v, records)
    return records


folder1 = 'C:/pythonCode/JsonCompare/testFile/Json/'
folder2 = 'C:/pythonCode/JsonCompare/testFile/Json/'

file = 'file1.json'

with open(f'{folder1}/{file}') as file_1, open(f'{folder2}/{file}') as file_2:
    data_1 = json.load(file_1)
    data_2 = json.load(file_2)

    records_1 = get_deep_records_by_report_id(data_1)
    records_2 = get_deep_records_by_report_id(data_2)

    for report_id, records in records_1.items():
        if report_id in records_2:
            for record1, record2 in zip(records, records_2[report_id]):
                differences = DeepDiff(record1, record2, ignore_order=True)
                if differences:
                    print(f'Differences between records in {file} under reportId {report_id}:')
                    print(differences)
        else:
            print(f"reportId {report_id} doesn't exist in second file")