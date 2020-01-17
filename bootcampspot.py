import requests

from settings import EMAIL, PASSWORD, COURSE_ID

BASE_URL = "https://bootcampspot.com/api/instructor/v1/"


class BootcampSpot:
    def __init__(self):
        self.auth_token = None
        self.login()

    def login(self) -> None:
        endpoint = "login"
        response = requests.post(BASE_URL + endpoint, json={'email': EMAIL, 'password': PASSWORD})
        response.raise_for_status()
        self.auth_token = response.json().get("authenticationInfo", {}).get("authToken", "")

    def get_assignments(self):
        endpoint = "grades"
        response = requests.post(BASE_URL + endpoint, json={'courseId': COURSE_ID},
                                 headers={'authToken': self.auth_token, 'Content-Type': 'application/json'})
        response.raise_for_status()
        return response.json()
