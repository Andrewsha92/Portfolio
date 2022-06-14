import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
redirect_count = len(response.history)
print(f"Количество перенаправлений - {redirect_count}")

for response in response.history:
    print(f"{response.url}")
print("Конечный URL")





