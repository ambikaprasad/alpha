from django.contrib import admin
from models import *
from django.conf import settings
from datetime import datetime

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description','slug','active','created_date','modified_date','added_by')
    list_editable = ('active',)
    exclude = ('slug','added_by')
    search_fields = ('tag_name',)
    def get_queryset(self, request):
        qs = super(CategoryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(added_by=request.user)
    def save_model(self, request, obj, form, change):
        obj.added_by=request.user
        obj.save()



admin.site.register(Category,CategoryAdmin)

