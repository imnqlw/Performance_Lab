import json

file = input()
#task3/value.json
bile = input()
#task3/test.json
report = input()
#task3/report.json

with open(file, 'r', encoding='utf-8') as f:
    val = json.load(f)

with open(bile, 'r', encoding='utf-8') as f:
    tes = json.load(f)

values_list = val.get("values", [])

values_dict = {item.get("id"): item.get("value") for item in values_list}


def fill_values(tes, values_dict):
    test_id = tes.get("id")
    if test_id is not None and test_id in values_dict:
        tes["value"] = values_dict[test_id]


    if "values" in tes and isinstance(tes["values"], list):
        for item in tes["values"]:
            fill_values(item, values_dict)


tests_list = tes.get("tests", [])
for test in tests_list:
    fill_values(test, values_dict)


with open('report.json', 'w', encoding='utf-8') as f:
    json.dump(tes, f, indent=4, ensure_ascii=False)

