"""User Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class User(Model):
    """User Model."""

    __fillable__ = ["username", "email", "password"]

    __auth__ = "username"

    ## Establish that users can have many dogs
    @has_many("id", "user_id")
    def dogs(self):
        from app.Dog import Dog
        return Dog

    ## Establish that users can have many owners
    @has_many("id", "user_id")
    def owners(self):
        from app.Owner import Owner
        return Owner
