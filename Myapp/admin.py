from django.contrib import admin
from . import models
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname","phone")
  
admin.site.register(models.Emp,MemberAdmin)
admin.site.register(models.Member)
admin.site.register(models.Contact)
admin.site.register(models.ValueStore)
admin.site.register(models.Register)
admin.site.register(models.name)
admin.site.register(models.Register_email)
admin.site.register(models.USER)
admin.site.register(models.Product_admin)
admin.site.register(models.Product_user)
admin.site.register(models.Quiz_questions)