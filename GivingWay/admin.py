
from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
class DonorAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="50" style="border-radius:10px"/>  '.format(object.donorpic.url))


    thumbnail.short_description="photo"
    list_display=("id","thumbnail","name","email","contact","address",)
    list_display_links=("name",)
    search_fields=("name",)
    list_filter=("address",)

admin.site.register(Donor,DonorAdmin)

class VolunteerAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="50" style="border-radius:10px"/>  '.format(object.volunteerpic.url))


    thumbnail.short_description="photo"
    list_display=("id","thumbnail","name","email","contact","address",)
    list_display_links=("name",)
    search_fields=("name",)
    list_filter=("address",)
admin.site.register(Volunteer,VolunteerAdmin)

class DonationAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="50" style="border-radius:10px"/>  '.format(object.donationpic.url))


    thumbnail.short_description="photo"
    list_display=("id","thumbnail","donationname",)
    list_display_links=("donationname",)
    # search_fields=("donationname",)
    # list_filter=("donationname",) 
admin.site.register(Donation,DonationAdmin)

admin.site.register(DonationArea)