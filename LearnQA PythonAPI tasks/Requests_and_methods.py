import requests

print("GET REQUESTS")
print("============")

data = ["GET", "POST", "PUT", "DELETE"]
for i in data:
    print(i, end=": ")
    params = {"method": i}
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=params)
    if i == "POST": # передаем POST в параметрах
        print(f"{response.text},{response.status_code}")
    if i == "GET":  # передаем GET в параметрах
        print(f"{response.text},{response.status_code}")
    if i == "PUT": # передаем PUT в параметрах
        print(f"{response.text},{response.status_code}")
    if i == "DELETE": # передаем DELETE в параметрах
        print(f"{response.text},{response.status_code}")
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", data="HEAD")
print(f"HEAD: {response.text},{response.status_code}")
print("============================================================")

print("POST REQUESTS")
print("=============")

data = ["POST", "GET", "PUT", "DELETE"]
for i in data:
    print(i, end=": ")
    params = {"method": i}
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=params)
    if i == "POST": # передаем POST в параметрах
        print(f"{response.text},{response.status_code}")
    if i == "GET": # передаем GET в параметрах
        print(f"{response.text},{response.status_code}")
    if i == "PUT": # передаем PUT в параметрах
        print(f"{response.text},{response.status_code}")
    if i == "DELETE": # передаем DELETE в параметрах
        print(f"{response.text},{response.status_code}")
print("============================================================")

"""PUT"""
print("PUT REQUESTS")
print("=============")

data = ["PUT", "GET", "POST", "DELETE"]
for i in data:
    print(i, end=": ")
    params = {"method": i}
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=params)
    if i == "PUT": # передаем PUT в параметрах
        print(f"{response.text},{response.status_code}")
    if i == "GET": # передаем GET в параметрах
        print(f"{response.text},{response.status_code}")
    if i == "POST": # передаем POST в параметрах
        print(f"{response.text},{response.status_code}")
    if i == "DELETE": # передаем DELETE в параметрах
        print(f"{response.text},{response.status_code}")
print("============================================================")

"""DELETE"""
print("DELETE REQUESTS")
print("================")

data = ["DELETE", "GET", "POST", "PUT"]
for i in data:
    print(i, end=": ")
    params = {"method": i}
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=params)
    if i == "DELETE": # передаем DELETE в параметрах
        print(f"{response.text},{response.status_code}")
    if i == "GET": # передаем GET в параметрах
        print(f"{response.text},{response.status_code}")
    if i == "POST": # передаем POST в параметрах
        print(f"{response.text},{response.status_code}")
    if i == "PUT": # передаем PUT в параметрах
        print(f"{response.text},{response.status_code}")
print("==============")

print("Тест завершен")
