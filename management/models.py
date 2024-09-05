from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MinValueValidator, MaxValueValidator

class InterviewPanel(models.Model):
    member_name = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
    password = models.CharField(max_length=200,default="ABC//123")

    def __str__(self):
        return self.member_name


class ApplicantData(models.Model):

    name = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    about = models.TextField(max_length=10000)

    application_status = models.CharField(max_length=50, default='Pending')
    interview_panel = models.ForeignKey(InterviewPanel,default=None,null=True,on_delete=models.CASCADE)
    scheduled_time_slot = models.DateTimeField(null=True, blank=True,default=None)
    feedback_text = models.TextField(null=True, blank=True,default=None)
    rating = models.IntegerField(null=True, blank=True,default=None,validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.scheduled_time_slot:
            if self.application_status not in ['Rejected', 'Selected']:
                self.application_status = 'Scheduled'
        
        super().save(*args, **kwargs)