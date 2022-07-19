from urllib.parse import urlparse


class BasePage(object):
    # Конструктор класса - специальный метод с ключевым словом __init__
    # Нам нужны объект вебдрайвера, адрес страницы и время ожидания вебэлементов
    def __init__(self, driver, url, time=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(time)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path
