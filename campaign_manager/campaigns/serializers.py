from rest_framework import serializers
from .models import Agent, Campaign, CampaignResult

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'agent_name', 'language', 'voice_id', 'updated', 'created_at']
        read_only_fields = ['updated', 'created_at']

class CampaignResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignResult
        fields = [
            'id', 'campaign', 'name', 'type', 'phone', 'cost',
            'outcome', 'call_duration', 'recording', 'summary',
            'transcription', 'created_at'
        ]
        read_only_fields = ['created_at']

class CampaignSerializer(serializers.ModelSerializer):
    results = CampaignResultSerializer(many=True, read_only=True)
    agent_name = serializers.CharField(source='agent.agent_name', read_only=True)

    class Meta:
        model = Campaign
        fields = [
            'id', 'campaign_name', 'type', 'phone_number',
            'status', 'agent', 'agent_name', 'results',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']