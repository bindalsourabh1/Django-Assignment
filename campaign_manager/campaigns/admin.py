# campaigns/admin.py

from django.contrib import admin
from .models import Agent, Campaign, CampaignResult

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('agent_name', 'language', 'voice_id', 'updated')
    search_fields = ('agent_name', 'voice_id')

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('campaign_name', 'type', 'status', 'agent')
    list_filter = ('type', 'status')
    search_fields = ('campaign_name',)

@admin.register(CampaignResult)
class CampaignResultAdmin(admin.ModelAdmin):
    list_display = ('name', 'campaign', 'type', 'outcome', 'call_duration')
    list_filter = ('outcome',)
    search_fields = ('name', 'campaign__campaign_name')