from django.contrib import admin
from .models import Jobs, users
# Register your models here.


admin.site.register(Jobs)
admin.site.register(users)


admin.site.site_header = "Job Portal Admin"