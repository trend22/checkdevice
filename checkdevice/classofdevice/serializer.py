from rest_framework.serializers import ModelSerializer

from .models import ClassOfDevice


# create serializer for work with DB
class ClassOfDeviceSerializer(ModelSerializer):
    class Meta:
        # create model of serializer
        model = ClassOfDevice
        # add all fields of CompanyCheck to serializer
        fields = '__all__'