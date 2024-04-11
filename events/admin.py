from django.contrib import admin
from .models import Venue, Event, Participant, Ticket, Speaker


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'venue')
    list_filter = ('start_time', 'end_time', 'venue')
    search_fields = ('name', 'description')
    filter_horizontal = ('speakers',)


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')


class TicketAdmin(admin.ModelAdmin):
    list_display = ('event', 'participant', 'purchase_time', 'price')
    list_filter = ('event', 'participant')
    search_fields = ('event__name', 'participant__name')


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Venue)
admin.site.register(Event, EventAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Speaker, SpeakerAdmin)
