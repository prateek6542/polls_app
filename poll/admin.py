from django.contrib import admin
from .models import Poll, Vote

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'total', 'option_one_count', 'option_two_count', 'option_three_count')

admin.site.register(Poll, PollAdmin)
admin.site.register(Vote)
