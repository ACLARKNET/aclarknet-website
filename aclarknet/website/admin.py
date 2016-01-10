from django.contrib import admin
from .models import Client
from .models import Service
from .models import TeamMember
from .models import Testimonial

# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """
    """


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    """


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    """
    """


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """
    """
