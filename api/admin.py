from django.contrib import admin
from .models import User,Booking,Advisor
''' 
    A module to make a models available to superuser.
    ...
    Attributes
    ----------
    AdvisorAdmin : class
    Registering Advisor model with admin
    UserAdmin: class
    Registering Advisor model with admin
    BookingAdmin : class
    Registering Advisor model with admin
'''
@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    list_display = ['id','advisorname','picture']
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','password','email']
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id','username','userid','advisorname','advisorid','time']
