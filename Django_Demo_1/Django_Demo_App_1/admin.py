from django.contrib import admin
from Django_Demo_App_1.models import AccessRecord,Webpage,Topic,UserProfileInfo
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)
admin.site.register(UserProfileInfo)
