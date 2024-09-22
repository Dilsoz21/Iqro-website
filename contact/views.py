from rest_framework import mixins, status
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from .serializers import *
import telebot
from config import settings

def send_telegram_message(message):
    bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN[0])
    bot.send_message(settings.TELEGRAM_CHANNEL_ID[0], message)

class ContactPagination(PageNumberPagination):   # always used in List!
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000


@extend_schema_view(
    list=extend_schema(summary='list contact project', tags=['Contact']),
    retrieve=extend_schema(summary='retrieve contact project', tags=['Contact']),
    create=extend_schema(summary='create contact project', tags=['Contact']),
    destroy=extend_schema(summary='destroy contact project', tags=['Contact']
))
class CRUDContact(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    pagination_class = ContactPagination


    def perform_create(self, serializer):
        instance = serializer.save()
        data = instance.create_at
        date = str(data)[0:10]
        time = str(data)[11:19]
        message = f"Contact ({date+"/"+time}): \nName: {instance.name}\nPhone: {instance.phone}\nEmail: {instance.email}\nMessage: {instance.message}"
        return send_telegram_message(message)



