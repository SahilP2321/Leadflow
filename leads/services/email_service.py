from django.core.mail import EmailMessage
from django.conf import settings
import os

class EmailService:
    def send_personalized_report(self, to_email, recipient_name, report_path):
        subject = f"Your Strategic Business Audit Report - {recipient_name}"
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ font-family: 'Segoe UI', Arial, sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .header {{ background: linear-gradient(135deg, #1a56db 0%, #1e3a8a 100%); color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0; }}
                .content {{ background: #fff; padding: 30px; border: 1px solid #e5e7eb; }}
                .footer {{ background: #f9fafb; padding: 20px; text-align: center; border-radius: 0 0 10px 10px; font-size: 12px; color: #6b7280; }}
                h1 {{ margin: 0; font-size: 28px; }}
                h2 {{ color: #1a56db; margin-top: 0; }}
                .button {{ background: #1a56db; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; display: inline-block; margin: 20px 0; }}
                .insight {{ background: #f0fdf4; padding: 15px; border-left: 4px solid #059669; margin: 15px 0; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>LeadFlow Automation</h1>
                    <p>Strategic Business Intelligence</p>
                </div>
                <div class="content">
                    <h2>Dear {recipient_name},</h2>
                    
                    <p>Thank you for requesting a business audit through LeadFlow. Based on your submission, we've prepared a comprehensive strategic report for your organization.</p>
                    
                    <div class="insight">
                        <strong>📊 Report Highlights:</strong><br>
                        • Complete company profile and market analysis<br>
                        • Strategic insights and growth opportunities<br>
                        • Technology stack assessment<br>
                        • Phased implementation roadmap<br>
                        • ROI projections and next steps
                    </div>
                    
                    <p>Your personalized report is attached to this email. This document provides actionable insights and recommendations tailored to your business needs.</p>
                    
                    <p style="margin-top: 25px;">We look forward to discussing how LeadFlow can help accelerate your growth.</p>
                    
                    <p>Best regards,<br>
                    <strong>LeadFlow Intelligence</strong></p>
                </div>
                <div class="footer">
                    <p>© 2024 LeadFlow Automation | Confidential Business Report</p>
                    <p>This is an automated message, please do not reply directly.</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        email = EmailMessage(
            subject=subject,
            body=html_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[to_email],
        )
        email.content_subtype = "html"
        
        if os.path.exists(report_path):
            with open(report_path, 'rb') as f:
                email.attach(f"LeadFlow_Report_{recipient_name}.pdf", f.read(), 'application/pdf')
        
        email.send()
        return True