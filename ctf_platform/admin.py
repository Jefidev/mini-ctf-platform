from django.contrib import admin

# Register your models here.
from ctf_platform.models import Team, Challenge, FlagSubmission


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled')
    list_filter = ('name', 'enabled',)
    ordering = ('name',)
    search_fields = ('name',)


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    ordering = ('title',)
    search_fields = ('title',)


class FlagSubmissionAdmin(admin.ModelAdmin):
    list_display = ('date', 'team', 'challenge', 'submitted', 'already_flagged')
    list_filter = ('date', 'team', 'challenge', 'already_flagged')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('team', 'challenge')


admin.site.register(Team, TeamAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(FlagSubmission, FlagSubmissionAdmin)
