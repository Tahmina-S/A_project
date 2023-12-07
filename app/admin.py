from django.contrib import admin
from app.models import Purchase_Model
# Register your models here.
@admin.register(Purchase_Model)

class Purchase_ModelAdmin(admin.ModelAdmin):
    list_display=['id','name','address','phone','email','photo']
    list_editable=['name','address','phone','email','photo' ]