from django.db import models
from django.core.validators import EmailValidator

class Lead(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('enriching', 'Enriching Company Data'),
        ('generating', 'Generating Report'),
        ('completed', 'Report Sent'),
        ('failed', 'Failed'),
    ]
    
    name = models.CharField(max_length=200)
    email = models.EmailField(validators=[EmailValidator()])
    company = models.CharField(max_length=300)
    position = models.CharField(max_length=200, blank=True)
    enriched_data = models.JSONField(default=dict, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    report_path = models.CharField(max_length=500, blank=True)
    error_message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-submitted_at']
    
    def __str__(self):
        return f"{self.name} - {self.company}"