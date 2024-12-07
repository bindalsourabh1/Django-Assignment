from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgentViewSet, CampaignViewSet, CampaignResultViewSet

router = DefaultRouter()
router.register(r'agents', AgentViewSet)
router.register(r'campaigns', CampaignViewSet)
router.register(r'campaign-results', CampaignResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]