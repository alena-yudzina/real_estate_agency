from django.contrib import admin
from .models import Flat, Сomplaint, Owner


class OwnersInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    list_filter = ('new_building',)
    raw_id_fields = ('liked_by',)
    inlines = [
        OwnersInline,
    ]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'author',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Сomplaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
