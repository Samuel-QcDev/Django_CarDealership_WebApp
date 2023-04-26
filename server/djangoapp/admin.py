from django.contrib import admin
from .models import CarModel, CarMake


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'year')
    list_filter = ['name']
    search_fields = ['name']
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')
    list_filter = ['name']
    search_fields = ['name']
# Register models here

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
