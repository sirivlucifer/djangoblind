from django.contrib import admin
from dagit.models import Gonderi, Kategori

class GonderiAdmin(admin.ModelAdmin):
    pass

class KategoriAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gonderi, GonderiAdmin)
admin.site.register(Kategori, KategoriAdmin)