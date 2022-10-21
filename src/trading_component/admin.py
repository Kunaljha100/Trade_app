from django.contrib import admin
from .models import order


class orderAdmin(admin.ModelAdmin):
    list_display= ('entry_price', "quantity", "trade_time", "trade_type","user")



admin.site.register(order)


# Register your models here.
