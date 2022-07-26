from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import TypeOfSi

from .serializer import TypeOfSiSerializer


class TypeOfSiViewSet(ModelViewSet):
    # get all company checks
    queryset = TypeOfSi.objects.all()
    serializer_class = TypeOfSiSerializer
    '''Для проверки аутентификации пользователя при запросах - IsAuthenticated'''
    '''IsAuthenticatedOrReadOnly - Get запросы доступны для незарегистрированных юзеров'''
    permission_classes = [IsAuthenticatedOrReadOnly]
    '''подключение фильтров'''
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'regNumber']
    search_fields = ['name', 'regNumber']
    ordering_field = ['name', 'regNumber']
