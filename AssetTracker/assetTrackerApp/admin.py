from django.contrib import admin
from assetTrackerApp.models import Company,Employee,Asset,AssetLog

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id','name','location','phone']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone','department','company']

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['id','name','model','brand','purchased_date','condition','issued']

@admin.register(AssetLog)
class AssetLogAdmin(admin.ModelAdmin):
    list_display =  ['id','asset','employee','checkout_date','return_date','checkout_condition','return_condition']
    

