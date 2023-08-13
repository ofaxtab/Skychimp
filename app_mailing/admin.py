from django.contrib import admin

from app_mailing.models import Mailing, Message, MailingTry


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('message', 'time', 'periodicity', 'status')
    list_filter = ('message', 'time', 'periodicity', 'status')
    search_fields = ('message',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    list_filter = ('title', 'body')
    search_fields = ('title', 'body')


@admin.register(MailingTry)
class MailingTryAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'try_datetime', 'try_status', 'mail_service_response')
    list_filter = ('mailing', 'try_datetime', 'try_status')
    search_fields = ('mail_service_response',)
