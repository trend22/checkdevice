from rest_framework.serializers import ModelSerializer

from .models import IntervalCheck


# create serializer for work with DB
class IntervalCheckSerializer(ModelSerializer):
    class Meta:
        # create model of serializer
        model = IntervalCheck
        # add all fields of CompanyCheck to serializer
        fields = '__all__'