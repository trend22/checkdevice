from rest_framework.serializers import ModelSerializer

from .models import CompanyUse


class CompanyUseSerializer(ModelSerializer):
    class Meta:
        model = CompanyUse
        fields = '__all__'
