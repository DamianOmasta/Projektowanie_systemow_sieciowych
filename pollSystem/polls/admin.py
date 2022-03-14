from django.contrib import admin
from .models import *

admin.site.register(Candidates)
admin.site.register(Votes)
admin.site.register(Positions)

# Register your models here.
