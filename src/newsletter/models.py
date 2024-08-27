from django.db import models


class EmailTemplate(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(verbose_name='HTML Content')


class EmailCampaign(models.Model):
    name = models.CharField(max_length=30)
    email_template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, default='pending')
    send_to_all = models.BooleanField(default=False)
    selected_users_ids = models.JSONField(null=True, blank=True)
    progress = models.IntegerField(default=0)
    sent_count = models.IntegerField(default=0)

