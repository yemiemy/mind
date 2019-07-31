from django.contrib import admin
from accounts.models import Team, Role, UserProfile

# Register your models here.
admin.site.register(Team),
admin.site.register(Role),
admin.site.register(UserProfile)