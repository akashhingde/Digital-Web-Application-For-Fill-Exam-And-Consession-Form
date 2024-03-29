from django.contrib import admin
from .models import *
admin.site.site_header= "SSJCOE ADMINISTRATION"
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user'  , 'admission_no' , 'full_name' , 'address' , 'gender' , 'age' ,  'mobile_no' ,'birth_date' , 'current_year' , 'category'  ]





admin.site.register(UserProfileModel, UserProfileAdmin)

admin.site.register(examformmodel)
admin.site.register(atktmodel)
admin.site.register(regularrevalutionmodel)
admin.site.register(atktrevalutionmodel)
admin.site.register(regularphotocopymodel)
admin.site.register(atktphotocopymodel)
admin.site.register(examcelladmin)
admin.site.register(consessionadmin)
admin.site.register(consessionformmodel)
admin.site.register(Branch)
admin.site.register(Year)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Subject_multiple)
admin.site.register(uploadresultmodel)
admin.site.register(uploadnoticemodel)
admin.site.register(newconsessionformmodel)




# Register your models here.
