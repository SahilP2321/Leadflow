from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Lead
from .tasks import process_lead_async

def lead_form(request):
    return render(request, 'leads/form.html')

def submit_lead(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            company = request.POST.get('company')
            position = request.POST.get('position', '')
            
            validate_email(email)
            
            if not all([name, email, company]):
                return JsonResponse({'error': 'Missing required fields'}, status=400)
            
            lead = Lead.objects.create(
                name=name,
                email=email,
                company=company,
                position=position
            )
            
            process_lead_async.delay(lead.id)
            
            if request.headers.get('HX-Request'):
                return render(request, 'leads/success.html', {'lead': lead})
            
            return JsonResponse({
                'success': True,
                'lead_id': lead.id,
                'message': 'Lead received! Processing your report...'
            })
            
        except ValidationError:
            return JsonResponse({'error': 'Invalid email address'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid method'}, status=405)

def lead_status(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)
    
    if request.headers.get('HX-Request'):
        return render(request, 'leads/status.html', {'lead': lead})
    
    return JsonResponse({
        'status': lead.status,
        'completed': lead.status == 'completed',
        'error': lead.error_message if lead.status == 'failed' else None
    })