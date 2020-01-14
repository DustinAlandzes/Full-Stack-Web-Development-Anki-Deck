import os
import random

import requests

BASE_URL = "https://bootcampspot.com/api/instructor/v1/"
COURSE_ID = os.environ.get('COURSE_ID')
EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')


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


