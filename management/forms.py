from django import forms
from .models import ApplicantData

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplicantData
        fields = ['name','email','about']

class ApplicantManageForm(forms.ModelForm):
    class Meta:
        model = ApplicantData
        fields = ['application_status', 'interview_panel', 'scheduled_time_slot','feedback_text','rating']

    def __init__(self, *args, **kwargs):
        super(ApplicantManageForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control border-primary'        