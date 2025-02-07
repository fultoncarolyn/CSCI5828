import unittest

from git_exercise.users.users_api import users_api
from git_exercise.users.users_gateway import UsersGateway
from tests.blueprint_test_support import test_client


class TestUsersApi(unittest.TestCase):
    def setUp(self):
        gateway = UsersGateway()
        self.client = test_client(users_api(gateway))

    def test_list(self):
        response = self.client.get("/users")

        self.assertEqual(200, response.status_code)
        self.assertIn(
            {
                "id": 1,
                "name": "Fred Derf",
                "email": "fred@example.com",
                "is_admin": True,
            },
            response.json,
        )

    def test_find(self):
        response = self.client.get("/users/2")

        self.assertEqual(200, response.status_code)
        self.assertEqual(
            {
                "id": 2,
                "name": "Mary Yram",
                "email": "mary@example.com",
                "is_admin": False,
            },
            response.json,
        )

    def test_find_not_found(self):
        response = self.client.get("/users/2345")

        self.assertEqual(404, response.status_code)

    def test_create(self):
        response = self.client.post(
            "/users", data={"name": "Kate Etak", "email": "kate@example.com"}
        )

        self.assertEqual(201, response.status_code)
        self.assertEqual({"id": 5}, response.json)

    def test_update(self):
        response = self.client.put(
            "/users/1", data={"name": "Paul Luap", "email": "paul@example.com"}
        )

        self.assertEqual(200, response.status_code)
        self.assertEqual(
            {
                "id": 1,
                "name": "Paul Luap",
                "email": "paul@example.com",
                "is_admin": True,
            },
            response.json,
        )

    def test_update_not_found(self):
        response = self.client.put(
            "/users/6", data={"name": "Paul Luap", "email": "paul@example.com"}
        )

        self.assertEqual(200, response.status_code)
        self.assertEqual(None, response.json)
