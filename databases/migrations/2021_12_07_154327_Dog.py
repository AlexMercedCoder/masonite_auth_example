"""Dog Migration."""

from masoniteorm.migrations import Migration


class Dog(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("dogs") as table:
            table.increments("id")
            table.string("name")
            ## Field to track which user created the item
            table.integer("user_id")
            ## Defining the field as a foreign key
            table.foreign("user_id").references("id").on("users")
            ## Create the field that will be the foreign key
            table.integer("owner_id")
            ## Foreign Key Field tracking id of related owner
            table.foreign("owner_id").references("id").on("owners")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("dogs")
