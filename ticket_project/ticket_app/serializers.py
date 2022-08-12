from rest_framework import serializers
from .models import Users, Devices, KnowledgeArticles, Tickets


class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ["password"]


class DeviceSerial(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = "__all__"


class TicketSerial(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = "__all__"


class KBSerial(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeArticles
        fields = "__all__"



