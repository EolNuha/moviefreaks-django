from django.contrib import admin
from .models import Movies, Tvshows, Comingsoon, Episodes
# Register your models here.

admin.site.register(Movies)
admin.site.register(Tvshows)
admin.site.register(Comingsoon)
admin.site.register(Episodes)

