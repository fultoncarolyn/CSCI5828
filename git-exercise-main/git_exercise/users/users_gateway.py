from git_exercise.users.user import User


class UsersGateway:
    users: list[User]

    def __init__(self):
        self.users = [
            User(id=1, name="Fred Derf", email="fred@example.com", is_admin=True),
            User(id=2, name="Mary Yram", email="mary@example.com", is_admin=False),
            User(id=3, name="Jane Enaj", email="jane@example.com", is_admin=False),
            User(id=4, name="John Nhoj", email="john@example.com", is_admin=False),
        ]

    def find(self, user_id: int) -> User | None:
        for user in self.users:
            if user.id == user_id:
                return user

        return None

    def list(self):
        return self.users

    def create_user(self, name, email, is_admin):
        user = User(id=len(self.users) + 1, name=name, email=email, is_admin=is_admin)
        self.users.append(user)
        return user

    def update_user(self, user_id, name, email):
        user = self.find(user_id)
        if user is not None:
            user.name = name
            user.email = email
            return user

        return None
