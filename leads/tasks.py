from celery import shared_task
from .models import Lead
from .services.enricher import CompanyEnricher
from .services.report_generator import PersonalizedReportGenerator
from .services.email_service import EmailService
from datetime import datetime
import os
from django.conf import settings

@shared_task
def process_lead_async(lead_id):
    try:
        lead = Lead.objects.get(id=lead_id)
        
        # Step 1: Enrich company data
        lead.status = 'enriching'
        lead.save()
        enricher = CompanyEnricher()
        enriched_data = enricher.enrich(lead.company)
        lead.enriched_data = enriched_data
        lead.save()
        
        # Step 2: Generate professional PDF report
        lead.status = 'generating'
        lead.save()
        generator = PersonalizedReportGenerator()
        reports_dir = os.path.join(settings.BASE_DIR, 'media', 'reports')
        os.makedirs(reports_dir, exist_ok=True)
        filename = f"lead_{lead_id}_{int(datetime.now().timestamp())}.pdf"
        report_path = os.path.join(reports_dir, filename)
        generator.generate_report(lead, enriched_data, report_path)
        lead.report_path = f"media/reports/{filename}"
        lead.save()
        
        # Step 3: Send email with report
        email_service = EmailService()
        email_service.send_personalized_report(lead.email, lead.name, report_path)
        
        # Step 4: Mark complete
        lead.status = 'completed'
        lead.processed_at = datetime.now()
        lead.save()
        
        return f"Lead {lead_id} completed successfully"
        
    except Exception as e:
        lead.status = 'failed'
        lead.error_message = str(e)
        lead.save()
        return f"Failed: {str(e)}"