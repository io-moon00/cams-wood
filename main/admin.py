from django.contrib import admin
from .models import Page, Image
# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['img_preview', '__str__']

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']    


admin.site.register(Image, ImageAdmin)
admin.site.register(Page, PageAdmin)