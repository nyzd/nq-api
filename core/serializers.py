from rest_framework import serializers
from django.core.validators import RegexValidator
from django.db import models
from core.rtl_languages import RTL_LANGUAGE_CODES

from core.models import Request, Notification


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            "id",
            "resource_controller",
            "resource_action",
            "resource_uuid",
            "status",
            "description",
            "message",
            "message_type",
            "created_at",
        ]
