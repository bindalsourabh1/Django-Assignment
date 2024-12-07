from django.db import models
from django.core.validators import RegexValidator

class Agent(models.Model):
    agent_name = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    voice_id = models.CharField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agent_name

class Campaign(models.Model):
    CAMPAIGN_TYPES = (
        ('inbound', 'Inbound'),
        ('outbound', 'Outbound'),
    )
    
    CAMPAIGN_STATUS = (
        ('running', 'Running'),
        ('paused', 'Paused'),
        ('completed', 'Completed'),
    )

    campaign_name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CAMPAIGN_TYPES)
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    status = models.CharField(max_length=10, choices=CAMPAIGN_STATUS, default='paused')
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.campaign_name

class CampaignResult(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='results')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    outcome = models.CharField(max_length=100)
    call_duration = models.FloatField(help_text="Call duration in seconds")
    recording = models.URLField(max_length=500)
    summary = models.TextField()
    transcription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.campaign.campaign_name} - {self.name}"