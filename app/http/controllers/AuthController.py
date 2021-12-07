"""A AuthController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.auth import Auth


class AuthController(Controller):

    def __init__(self, request: Request, auth: Auth):
        ## Add Request and Auth as instance properties each route can use
        self.request = request
        self.auth = auth

    def login(self):
        username = self.request.input("username")
        password = self.request.input("password")
        result = self.auth.login(username, password)
        return result

    def signup(self):
        username = self.request.input("username")
        email = self.request.input("email")
        password = self.request.input("password")
        result = self.auth.register({"username": username, "email": email, "password": password})
        return result

    def logout(self):
        self.auth.logout()
        return "Logged Out"

