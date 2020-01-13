from typing import List
from unittest import TestCase

from bootcampspot import BootcampSpot
from fetch_assignments_create_issues import create_issues_for_assignments


class TestBootcampSpot(TestCase):
    def setUp(self) -> None:
        self.client = BootcampSpot()

    def test_login(self):
        self.client.login()
        self.assertEqual(type(self.client.auth_token), str)

    def test_get_assignments(self):
        self.assertEqual(type(self.client.get_assignments()), list)


class TestCreateIssues(TestCase):
    def test_create_issues_for_assignments(self):
        self.assertEqual(type(create_issues_for_assignments()), list)


