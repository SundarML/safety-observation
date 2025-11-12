from django.contrib import admin

# Register your models here.
# observations/admin.py
from django.contrib import admin
from .models import Observation, Location

@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ('title','location','severity','status','assigned_to','date_observed')
    list_filter = ('status','severity','location')
    search_fields = ('title','description')

admin.site.register(Location)
