from django.contrib import admin
from .models import CustomUser, Organization, Appointment


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "phone", "email", "is_hospital")
    search_fields = ("name", "email")
    list_filter = ("is_hospital",)


admin.site.register(Organization, OrganizationAdmin)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "organization")
    search_fields = ("username", "first_name", "last_name", "email")
    list_filter = ("organization", "is_staff", "is_superuser", "is_active")


admin.site.register(CustomUser, CustomUserAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "date", "time", "description")
    search_fields = ("patient__username", "description")
    list_filter = ("date", "time")
    date_hierarchy = "date"


admin.site.register(Appointment, AppointmentAdmin)
