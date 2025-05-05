import json
import sys




def fill_values(tes, values_dict):
    test_id = tes.get("id")
    if test_id is not None and test_id in values_dict:
        tes["value"] = values_dict[test_id]


    if "values" in tes and isinstance(tes["values"], list):
        for item in tes["values"]:
            fill_values(item, values_dict)




def generate_report(values_file, tests_file, report_file):
    with open(values_file, 'r', encoding='utf-8') as f:
        val = json.load(f)

    with open(tests_file, 'r', encoding='utf-8') as f:
        tes = json.load(f)

    values_list = val.get("values", [])

    values_dict = {item.get("id"): item.get("value") for item in values_list}
    tests_list = tes.get("tests", [])
    for test in tests_list:
        fill_values(test, values_dict)

    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(tes, f, indent=4, ensure_ascii=False)





if __name__ == '__main__':
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    generate_report(values_file, tests_file, report_file)