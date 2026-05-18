from django.urls import path
from . import views

urlpatterns = [
    path('', views.lead_form, name='lead_form'),
    path('submit-lead/', views.submit_lead, name='submit_lead'),
    path('lead-status/<int:lead_id>/', views.lead_status, name='lead_status'),
]