from rest_framework.serializers import ModelSerializer

from .models import TypeOfSi


# create serializer for work with DB
class TypeOfSiSerializer(ModelSerializer):
    class Meta:
        # create model of serializer
        model = TypeOfSi
        # add all fields of CompanyCheck to serializer
        fields = '__all__'