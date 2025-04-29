import json
import tempfile
import os

file = 'E:/proect/НТ Performance Lab/task3/value.json'
bile = 'E:/proect/НТ Performance Lab/task3/test.json'

# with open(file, 'r', encoding='utf-8') as f:
#     val = json.load(f)
#
# with open(bile, 'r', encoding='utf-8') as f:
#     tes = json.load(f)
#     # print(tes['tests'][0]['value'])


# def make_report(baza):
#     for i in range(2):
#         report = tes['tests'][i]
#         for key, value in report.items():
#             if key == 'id':
#                 for i in range(2):
#                     va = val['values'][i]
#                     with open("E:/proect/НТ Performance Lab/task3/report.json", "rb+", encoding="utf-8") as bile:
#
#
#                     report['value'] = va['value']
#     return report
#
#
# s = make_report(tes)
#
# with open("E:/proect/НТ Performance Lab/task3/report.json", "rb+", encoding="utf-8") as ile:
#
#     f.seek()
#     f.write()

with open(bile) as json_file:
    json_data = json.load(json_file)

    values = json_data['tests']
    for value in values:
        value['value'] = 'right'
    valus = json_data['tests']['values']
    for value in valus:
        value['value'] = 'right'



with open('report.json', "w") as f:
    json.dump(json_data, f)