from django.contrib import admin
from colorplat_trading.models import ColorPlat,ColorPrice,Trade

# Register your models here.
class ColorPlatAdmin(admin.ModelAdmin):
    list_display = ['name', 'rvalue','gvalue','bvalue','currentprice','CreatedAt'] 

class ColorPriceAdmin(admin.ModelAdmin):
    list_display = ['CreatedAt','priceRed','priceGreen','priceBlue'] 

admin.site.register(ColorPlat,ColorPlatAdmin)
admin.site.register(ColorPrice,ColorPriceAdmin)
admin.site.register(Trade)
