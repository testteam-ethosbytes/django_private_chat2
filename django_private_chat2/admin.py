# -*- coding: utf-8 -*-

from django.contrib.admin import ModelAdmin, site
from .models import MessageModel, DialogsModel


class MessageModelAdmin(ModelAdmin):
    readonly_fields = ('created', 'modified',)
    search_fields = ('id', 'text', 'sender__pk', 'recipient__pk')
    list_display = ('id', 'sender', 'recipient', 'text', 'get_files', 'read')
    list_display_links = ('id',)
    list_filter = ('sender', 'recipient')
    date_hierarchy = 'created'

    def get_files(self, obj):
        files = obj.file.all()
        if not files:
            return None
        return "\n".join([f.file.name for f in obj.file.all()])

    get_files.short_description = "Files"


class DialogsModelAdmin(ModelAdmin):
    readonly_fields = ('created', 'modified',)
    search_fields = ('id', 'user1__pk', 'user2__pk')
    list_display = ('id', 'user1', 'user2')
    list_display_links = ('id',)
    date_hierarchy = 'created'


site.register(DialogsModel, DialogsModelAdmin)
site.register(MessageModel, MessageModelAdmin)
