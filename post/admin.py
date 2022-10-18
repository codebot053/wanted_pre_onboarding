from django.contrib import admin

# local
from .models import Company, Technology, Post


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class JobPostingAdmin(admin.ModelAdmin):
    pass