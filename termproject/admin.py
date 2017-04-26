# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Note
from .models import Rating
from .models import Song
# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    model = Note
    fields = ['song', 'onset', 'pitch', 'volume', 'duration', 'channel', 'avg_rating', ]
    list_display = ['song', 'id', 'avg_rating', ]


admin.site.register(Note, NoteAdmin)
admin.site.register(Rating)
admin.site.register(Song)
