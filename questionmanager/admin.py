from django.contrib import admin
from models import *
from django.conf import settings
from datetime import datetime

class TagAdmin(admin.ModelAdmin):
    list_display = ('name','description','slug','active','is_category','created_date','modified_date','added_by')
    list_editable = ('active','slug')
    exclude = ('slug','added_by')
    search_fields = ('name',)
    def get_queryset(self, request):
        qs = super(TagAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(added_by=request.user)
    def save_model(self, request, obj, form, change):
        obj.added_by=request.user
        obj.save()

class QuestionManagerAdmin(admin.ModelAdmin):
    list_display = ('questype','question','parentquestion','category','tag','status','correct_answer','explanation','user','slug','default_marks','random_option','added_date','added_by')
    search_fields = ('question',)
    exclude = ('slug','added_by')
    def save_model(self, request, obj, form, change):
        obj.added_by=request.user
        obj.save()
class OptionAdmin(admin.ModelAdmin):
    list_display = ('question','option','active')
    search_fields = ('question__question')
    exclude = ('slug','added_by')



admin.site.register(Tag,TagAdmin)
admin.site.register(QuestionManager,QuestionManagerAdmin)
admin.site.register(Option,OptionAdmin)

