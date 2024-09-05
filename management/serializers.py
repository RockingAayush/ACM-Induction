from rest_framework import serializers
from .models import ApplicantData, InterviewPanel

class ApplicantDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantData
        fields = '__all__'

class InterviewPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewPanel
        exclude = ['password']
