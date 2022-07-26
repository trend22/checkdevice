from rest_framework.serializers import ModelSerializer

from .models import CompanyCheck


# create serializer for work with DB
class CompanyCheckSerializer(ModelSerializer):
    class Meta:
        # create model of serializer
        model = CompanyCheck
        # add all fields of CompanyCheck to serializer
        fields = '__all__'
