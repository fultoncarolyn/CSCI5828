import unittest

from git_exercise.users.user import User
from git_exercise.users.users_gateway import UsersGateway


class TestUsersGateway(unittest.TestCase):
    def test_list(self):
        gateway = UsersGateway()

        result = gateway.list()

        self.assertEqual(4, len(result))
        self.assertIn(
            User(id=1, name="Fred Derf", email="fred@example.com", is_admin=True),
            result,
        )

    def test_find(self):
        gateway = UsersGateway()

        self.assertEqual(
            User(id=2, name="Mary Yram", email="mary@example.com", is_admin=False),
            gateway.find(2),
        )
        self.assertIsNone(gateway.find(1234))
