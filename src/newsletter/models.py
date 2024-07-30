from django.db import models
from src.users.models import User


class EmailTemplate(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(verbose_name='HTML Content')


class EmailCampaign(models.Model):
    name = models.CharField(max_length=30)
    email_template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class UserEmailCampaign(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    email_campaign_id = models.ForeignKey(EmailCampaign, on_delete=models.CASCADE)


