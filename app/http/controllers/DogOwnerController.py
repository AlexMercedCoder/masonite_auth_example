"""A DogOwnerController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Dog import Dog
from app.Owner import Owner


class DogOwnerController(Controller):
    """DogOwnerController Controller Class."""

    def __init__(self, request: Request):
        """DogOwnerController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def get_user_owners(self):
        return self.request.user().owners
        
    def get_user_dogs(self):
        return self.request.user().dogs

    def create_owner(self):
        user = self.request.user()
        name = self.request.input("name")
        print(user)
        owner = Owner.create(name=name, user_id=user["id"])
        return owner

    def create_dog(self):
        user = self.request.user()
        name = self.request.input("name")
        owner_id = self.request.input("owner_id")
        dog = Dog.create(name=name, owner_id=owner_id, user_id=user.id)
        return dog
