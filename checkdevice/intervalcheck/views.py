from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet


from .models import IntervalCheck
from .permissions import IsUserOrStuffOnly

from .serializer import IntervalCheckSerializer


class IntervalCheckViewSet(ModelViewSet):
    # get all company checks
    queryset = IntervalCheck.objects.all()
    serializer_class = IntervalCheckSerializer
    '''Для проверки аутентификации пользователя при запросах - IsAuthenticated'''
    '''IsAuthenticatedOrReadOnly - Get запросы доступны для незарегистрированных юзеров'''
    permission_classes = {IsUserOrStuffOnly}
    '''подключение фильтров'''
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['interval']
    search_fields = ['interval']
    ordering_field = ['interval']
