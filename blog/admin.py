from django.contrib import admin
from . models import *

admin.site.site_header = 'Zago Hub'
admin.site.site_title = 'Welcome to the zone'
admin.site.index_title = 'Zago King'


admin.site.register(Post)
