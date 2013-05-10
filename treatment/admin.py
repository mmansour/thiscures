from treatment.models import TreatmentPage
from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin


class TreatmentPageAdmin(DisplayableAdmin):

    fieldsets = [
        ("Title",                       {'fields': ['title']}),
        ("Title Casing?",            {'fields': ['is_title_case']}),
        ("Published Date",              {'fields': ['publish_date']}),
        ("Published Status",            {'fields': ['status']}),
        ("Allow Comments",            {'fields': ['allow_comments']}),
        ("Subject Data",                 {'fields': ['subject_data']}),
        ("Subject Treatments",                 {'fields': ['subject_data_treatment']}),
        ("Subject Natural Cures",                 {'fields': ['subject_data_natural_cures']}),
        ("Subject Video",            {'fields': ['subject_video']}),
        ("Subject Image",            {'fields': ['subject_image']}),
        ("Subject Ad One",            {'fields': ['subject_one_ad']}),
        ("Data Sources",            {'fields': ['subject_data_sources']}),
    ]

    list_display = ('title', 'status', 'publish_date', 'allow_comments',)
    list_editable = ('status', 'allow_comments')
    list_filter = ['status', 'publish_date',]
    search_fields = ['title',]
    date_hierarchy = 'publish_date'

admin.site.register(TreatmentPage, TreatmentPageAdmin)

