from django.contrib import admin
from .models import Venue
from .models import Event
from .models import User

# Register your models here.

admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(User)