import requests
import pytest


class TestUserAgent:
    headers = [
        {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"},
        {"User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"},
        {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"},
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"},
        {"User-Agent": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
              ]

    @pytest.mark.parametrize('headers', headers)
    def test_check_user_agent(self, headers):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        response = requests.get(url, headers=headers)
        res_dict = response.json()

        platform = res_dict['platform']
        browser = res_dict['browser']
        device = res_dict['device']

        assert platform == res_dict['platform']
        assert browser == res_dict['browser']
        assert device == res_dict['device']

        # Dd = res_dict['platform']
        # Ee = res_dict['browser']
        # Ff = res_dict['device']
        #
        # assert Dd == 'Mobile'
        # assert Ee == 'Chrome'
        # assert Ff == 'iOS'
        #
        # Gg = res_dict['platform']
        # Hh = res_dict['browser']
        # Ii = res_dict['device']
        #
        # assert Gg == 'Googlebot'
        # assert Hh == 'Unknown'
        # assert Ii == 'Unknown'
        #
        # Jj = res_dict['platform']
        # Kk = res_dict['browser']
        # Ll = res_dict['device']
        #
        # assert Jj == 'Web'
        # assert Kk == 'Chrome'
        # assert Ll == 'No'
        #
        # Mm = res_dict['platform']
        # Nn = res_dict['browser']
        # Oo = res_dict['device']
        #
        # assert Mm == 'Web'
        # assert Nn == 'No'
        # assert Oo == 'iPhone'




















        #
# @pytest.mark.parametrize('headers', headers = {"User-Agent": [
#                                  "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
#
#                                  "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
#
#                                  "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
#
#                                  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
#
#                                  "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"]















