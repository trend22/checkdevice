# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .models import Device
from .serializer import DeviceSerializer


class DeviceViewSet(ModelViewSet):
    # get all company uses
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    '''Для проверки аутентификации пользователя при запросах - IsAuthenticated'''
    '''IsAuthenticatedOrReadOnly - Get запросы доступны для незарегистрированных юзеров'''
    # permission_classes = [IsUserOrStuffOnly]
    # '''подключение фильтров'''
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['name']
    # search_fields = ['name']
    # ordering_field = ['name']
