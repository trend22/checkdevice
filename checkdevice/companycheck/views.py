from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import CompanyCheck
from .permissions import IsUserOrStuffOnly

from .serializer import CompanyCheckSerializer


class CompanyCheckViewSet(ModelViewSet):
    # get all company checks
    queryset = CompanyCheck.objects.all()
    serializer_class = CompanyCheckSerializer
    '''Для проверки аутентификации пользователя при запросах - IsAuthenticated'''
    '''IsAuthenticatedOrReadOnly - Get запросы доступны для незарегистрированных юзеров'''
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [IsUserOrStuffOnly]
    '''подключение фильтров'''
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_field = ['name']
