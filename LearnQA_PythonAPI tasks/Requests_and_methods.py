import requests

print("GET REQUESTS")
print("=============")

data = ["GET", "POST", "PUT", "DELETE"]
for i in data:
    params = {"method": i}
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=params)
    res = response.url
    if "GET" in res:
        print(f"Запрос GET с параметрами - {response.text},{response.status_code}")
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
        print(f"Запрос GET без параметров - {response.text},{response.status_code}")
    if "POST" in res:
        print(f"Запрос GET, POST в параметрах - {response.text},{response.status_code}")
    if "PUT" in res:
        print(f"Запрос GET, PUT в параметрах - {response.text},{response.status_code}")
    if "DELETE" in res:
        print(f"Запрос GET, DELETE в параметрах - {response.text},{response.status_code}")
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", data="HEAD")
print(f"Запрос GET, HEAD в параметрах - {response.text},{response.status_code}")
print("============================================================")

print("POST REQUESTS")
print("=============")

data = ["POST", "GET", "PUT", "DELETE"]
for i in data:
    params = {"method": i}
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=params)
    if i == "POST":
        print(f"Запрос POST c параметрами - {response.text},{response.status_code}")
    if i == "GET":
        print(f"Запрос POST, GET в параметрах - {response.text},{response.status_code}")
    if i == "PUT":
        print(f"Запрос POST, PUT в параметрах - {response.text},{response.status_code}")
    if i == "DELETE":
        print(f"Запрос POST, DELETE в параметрах - {response.text},{response.status_code}")
print("============================================================")

"""PUT"""
print("PUT REQUESTS")
data = ["PUT", "GET", "POST", "DELETE"]
for i in data:
    params = {"method": i}
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=params)
    if i == "PUT":
        print(f"Запрос PUT c параметрами - {response.text},{response.status_code}")
    if i == "GET":
        print(f"Запрос PUT, GET в параметрах - {response.text},{response.status_code}")
    if i == "POST":
        print(f"Запрос PUT, POST в параметрах - {response.text},{response.status_code}")
    if i == "DELETE":
        print(f"Запрос PUT, DELETE в параметрах - {response.text},{response.status_code}")
print("============================================================")

"""DELETE"""
print("DELETE REQUESTS")
data = ["DELETE", "GET", "POST", "PUT"]
for i in data:
    params = {"method": i}
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=params)
    if i == "DELETE":
        print(f"Запрос DELETE c параметрами - {response.text},{response.status_code}")
    if i == "GET":
        print(f"Запрос DELETE, GET в параметрах - {response.text},{response.status_code}")
    if i == "POST":
        print(f"Запрос DELETE, POST в параметрах - {response.text},{response.status_code}")
    if i == "DELETE":
        print(f"Запрос DELETE, PUT в параметрах - {response.text},{response.status_code}")
print("==============")

print("Тест завершен")
