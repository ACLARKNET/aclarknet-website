from django.contrib import admin
from .models import Developer
from .models import Page
from .models import Partner
from .models import Service
from .models import Testimonial

# Register your models here.


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    """


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    """
    """


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """
    """
    prepopulated_fields = {"slug": ("name", )}


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    """
    """


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """
    """
