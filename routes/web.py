"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Post("/login", "AuthController@login").name("login"),
        Post("/signup", "AuthController@signup").name("signup"),
        Post("/logout", "AuthController@logout").name("logout"),
    ], prefix="/auth"),

    RouteGroup([
        Get("/dog", "DogOwnerController@get_user_dogs").name("get_dogs"),
        Get("/owners", "DogOwnerController@get_user_owners").name("get_owners"),
        Post("/owner", "DogOwnerController@create_owner").name("create_owner"),
        Post("/dog", "DogOwnerController@create_dog").name("create_dog"),
    ], prefix="/dogowner",middleware=["auth"])
]
