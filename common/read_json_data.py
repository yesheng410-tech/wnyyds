import json


def read_json():
    with open('../data/data_json', encoding='utf-8') as f:
        json_data = json.load(f)
        list_data = []
        for i in json_data:
            list_data.append(tuple(i.values()))

    return list_data


