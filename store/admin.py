from django.contrib import admin
from .models import *


admin.site.register(Flower)
admin.site.register(Order)
admin.site.register(Favorite)
admin.site.register(FavioriteItem)