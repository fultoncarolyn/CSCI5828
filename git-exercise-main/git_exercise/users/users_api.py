from flask import Blueprint, abort, jsonify, request

from git_exercise.users.users_gateway import UsersGateway


def users_api(users_gateway: UsersGateway) -> Blueprint:
    api = Blueprint("users_api", __name__)

    @api.route("/users")
    def list_all():
        return jsonify(users_gateway.list())

    @api.route("/users/<int:user_id>")
    def find(user_id: int):
        user = users_gateway.find(user_id)
        if user is None:
            abort(404)

        return jsonify(user)

    @api.route("/users", methods=["POST"])
    def create_user():
        name = request.form.get("name")
        email = request.form.get("email")
        is_admin = request.form.get("is_admin", False)

        user = users_gateway.create_user(name, email, is_admin)
        return jsonify({"id": user.id}), 201

    @api.route("/users/<int:user_id>", methods=["PUT"])
    def update_user(user_id: int):
        name = request.form.get("name")
        email = request.form.get("email")
        user = users_gateway.update_user(user_id, name, email)
        return jsonify(user), 200

    return api
