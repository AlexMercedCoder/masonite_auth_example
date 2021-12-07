"""Owner Migration."""

from masoniteorm.migrations import Migration


class Owner(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("owners") as table:
            table.increments("id")
            table.string("name")
            ## Field to track which user created the item
            table.integer("user_id")
            ## Defining the field as a foreign key
            table.foreign("user_id").references("id").on("users")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("owners")
