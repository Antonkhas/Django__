from django.contrib import admin

from .models import Orders, TicketsSupport, AccumulativePoints, Users, ShippingAddress

admin.site.register(Orders)
admin.site.register(TicketsSupport)
admin.site.register(AccumulativePoints)
admin.site.register(Users)
admin.site.register(ShippingAddress)