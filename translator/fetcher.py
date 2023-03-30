import requests


def get_html(link: str) -> str:
    with requests.Session() as rs:
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        headers = {'User-Agent': user_agent}
        try:
            res = rs.get(link, headers=headers)
            if res.status_code != 200:
                raise Exception("Wrong answer")
            return res.content.decode()
        except requests.exceptions.ConnectionError:
            raise Exception("Could not connect")
