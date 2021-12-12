"""Owner Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many

class Owner(Model):
    
    @has_many("id", "owner_id")
    def dogs(self):
        from app.Dog import Dog
        return Dog