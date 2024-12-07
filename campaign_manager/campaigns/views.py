from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from .models import Agent, Campaign, CampaignResult
from .serializers import AgentSerializer, CampaignSerializer, CampaignResultSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all().order_by('-created_at')
    serializer_class = AgentSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Agent.objects.all()
        agent_name = self.request.query_params.get('agent_name', None)
        if agent_name:
            queryset = queryset.filter(agent_name__icontains=agent_name)
        return queryset

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all().order_by('-created_at')
    serializer_class = CampaignSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Campaign.objects.all()
        campaign_name = self.request.query_params.get('campaign_name', None)
        status = self.request.query_params.get('status', None)
        
        if campaign_name:
            queryset = queryset.filter(campaign_name__icontains=campaign_name)
        if status:
            queryset = queryset.filter(status=status)
            
        return queryset

class CampaignResultViewSet(viewsets.ModelViewSet):
    queryset = CampaignResult.objects.all().order_by('-created_at')
    serializer_class = CampaignResultSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CampaignResult.objects.all()
        campaign_id = self.request.query_params.get('campaign', None)
        if campaign_id:
            queryset = queryset.filter(campaign_id=campaign_id)
        return queryset