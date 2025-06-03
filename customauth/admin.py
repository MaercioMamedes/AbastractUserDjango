from django.contrib import admin
from .models import MyUser


class Meta:
    model = MyUser
    fields = "_all_"

admin.site.register(MyUser)
