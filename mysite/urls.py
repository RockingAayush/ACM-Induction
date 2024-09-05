from django.contrib import admin
from django.urls import path,include
from management.views import *

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'applicants', ApplicantDataViewSet)
router.register(r'interview-panels', InterviewPanelViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',select,name="select"),
    path('application_form/',application_form,name="application_form"),
    path('success/',success,name="success"),

    # Dashboard base
    path('dashboard/',dashboard,name="dashboard"),
    path('login/',login,name="login"),
    path('logout/',logout,name="logout"),

    # Management
    path('applicant/<int:applicant_id>/manage/',manage_applicant, name='manage_applicant'),
    path('applicant/<int:applicant_id>/select/',select_applicant, name='select_applicant'),
    path('applicant/<int:applicant_id>/reject/',reject_applicant, name='reject_applicant'),

    path('notify-scheduled/', notify_scheduled_applicants, name='notify_scheduled_applicants'),
    path('notify-selected/', notify_selected_applicants, name='notify_selected_applicants'),
    path('notify-rejected/', notify_rejected_applicants, name='notify_rejected_applicants'),

    path('interview-panels/', interview_panels, name='interview_panels'),
    path('induction-report/', generate_report, name='induction_report'),
    path('api-docs/', api_docs, name="api_docs"),

    # API
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
