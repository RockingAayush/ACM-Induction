from django.shortcuts import render,redirect,get_object_or_404
from .models import ApplicantData,InterviewPanel
from .forms import ApplicationForm,ApplicantManageForm
from django.db import IntegrityError
from django.contrib import messages

from django.core.mail import send_mail
from django.db.models import Count

from rest_framework import viewsets
from .serializers import ApplicantDataSerializer, InterviewPanelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import SAFE_METHODS, BasePermission

# Base views
def select(request):
    return render(request,'select.html')

def success(request):
    return render(request,'success.html')

def application_form(request):
    form = ApplicationForm(request.POST or None)

    if form.is_valid():
        try:
            form.save()
            return redirect('success')
        
        except IntegrityError:
            form.add_error('email', 'A user with this email already has an account.')
     
    return render(request,'application_form.html',{'form':form})

def login(request):
    if request.method == 'POST':
        member_name = request.POST.get('member_name')
        password = request.POST.get('password')
        print(member_name,password)
        try:
            panel = InterviewPanel.objects.get(member_name=member_name)
            request.session['is_authenticated'] = True
            request.session['member_name'] = member_name 
            if panel.password == password:
                return redirect('dashboard')  
            else:
                messages.error(request, 'Invalid password. Please try again.')
        except InterviewPanel.DoesNotExist:
            messages.error(request, 'Panel member with this name does not exist.')

    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login')

def dashboard(request):

    if not request.session.get('is_authenticated'):
        return redirect('login')
    
    all_applicants = ApplicantData.objects.all()
    number_of_applicants = ApplicantData.objects.count()
    pending_applicants = ApplicantData.objects.filter(application_status='Pending').count()
    scheduled_applicants = ApplicantData.objects.filter(application_status='Scheduled').count()
    
    context = {
        'all_applicants':all_applicants,
        'number_of_applicants':number_of_applicants,
        'pending_applicants':pending_applicants,
        'scheduled_applicants':scheduled_applicants,
    }

    return render(request,'dashboard.html',context)


def manage_applicant(request, applicant_id):
    applicant = get_object_or_404(ApplicantData, id=applicant_id)
    form = ApplicantManageForm(request.POST or None, instance=applicant)

    if form.is_valid():
        form.save()
        return redirect('dashboard')  

    context = {
        'applicant': applicant,
        'form': form,
    }
    return render(request, 'manage_applicant.html', context)

def select_applicant(request, applicant_id):
    applicant = get_object_or_404(ApplicantData, id=applicant_id)
    applicant.application_status = 'Selected'
    applicant.save()
    return redirect('dashboard')

def reject_applicant(request, applicant_id):
    applicant = get_object_or_404(ApplicantData, id=applicant_id)
    applicant.application_status = 'Rejected'
    applicant.save()
    return redirect('dashboard')


# Auto Email views
def send_email_to_scheduled():
    applicants = ApplicantData.objects.filter(application_status='Scheduled')
    for applicant in applicants:
        send_mail(
            'Interview Scheduled',
            f'Dear {applicant.name},\n\nYour interview is scheduled on {applicant.scheduled_time_slot}.\n\nYour interviewer is {applicant.interview_panel}',
            'rastogi.bkn@gmail.com',
            [applicant.email],
            fail_silently=False,
        )


def send_email_to_selected():
    applicants = ApplicantData.objects.filter(application_status='Selected')
    for applicant in applicants:
        send_mail(
            'Congratulations, You are Selected!',
            f'Dear {applicant.name},\n\nWe are pleased to inform you that you have been selected.\n\nWelcome to the family, join our whatsapp group:any_link',
            'rastogi.bkn@gmail.com',
            [applicant.email],
            fail_silently=False,
        )

def send_email_to_rejected():
    applicants = ApplicantData.objects.filter(application_status='Rejected')
    for applicant in applicants:
        send_mail(
            'Interview Result: Not Selected',
            f'Dear {applicant.name},\n\nWe regret to inform you that you have not been selected.\n\nBetter luck next time. :)',
            'rastogi.bkn@gmail.com',
            [applicant.email],
            fail_silently=False,
        )

def notify_scheduled_applicants(request):
    send_email_to_scheduled()
    return redirect('dashboard')

def notify_selected_applicants(request):
    send_email_to_selected()
    return redirect('dashboard')

def notify_rejected_applicants(request):
    send_email_to_rejected()
    return redirect('dashboard')

# Misc Dashboard functions
def interview_panels(request):
    panels = InterviewPanel.objects.all()
    return render(request, 'interview_panels.html', {'panels': panels})

def generate_report(request):
    
    total_applicants = ApplicantData.objects.count()
    status_summary = ApplicantData.objects.values('application_status').annotate(count=Count('application_status'))
    panels = InterviewPanel.objects.all()
    scheduled_interviews = ApplicantData.objects.filter(application_status='Scheduled').order_by('scheduled_time_slot')
    feedback_summary = ApplicantData.objects.exclude(feedback_text=None)

    context = {
        'total_applicants': total_applicants,
        'status_summary': status_summary,
        'panels': panels,
        'scheduled_interviews': scheduled_interviews,
        'feedback_summary': feedback_summary,
    }

    return render(request, 'induction_report.html', context)

def api_docs(request):
    return render(request,'api_docs.html')

# API
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
   
class ApplicantDataViewSet(viewsets.ModelViewSet):
    queryset = ApplicantData.objects.all()
    serializer_class = ApplicantDataSerializer
    permission_classes = [IsAuthenticated,ReadOnly]

class InterviewPanelViewSet(viewsets.ModelViewSet):
    queryset = InterviewPanel.objects.all()
    serializer_class = InterviewPanelSerializer
    permission_classes = [IsAuthenticated,ReadOnly]  