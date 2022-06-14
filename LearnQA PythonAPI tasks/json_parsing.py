import json

string_as_json_format = '{"code": "https://github.com/Andrewsha92/Portfolio.git"}'
obj = json.loads(string_as_json_format)
json_text = obj["code"]

key = "code1"

if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON нет!")





















