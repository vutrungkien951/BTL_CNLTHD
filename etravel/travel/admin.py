from django.contrib import admin
from .models import User, Ride, Port, FeedBack


# Register your models here.

admin.site.register(User)
admin.site.register(Ride)
admin.site.register(Port)
admin.site.register(FeedBack)