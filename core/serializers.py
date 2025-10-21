from rest_framework import serializers
from django.core.validators import RegexValidator
from django.db import models
from core.rtl_languages import RTL_LANGUAGE_CODES

from core.models import ErrorLog, PhraseTranslation, Phrase, Notification

class ErrorLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorLog
        fields = '__all__'

class PhraseTranslationSerializer(serializers.ModelSerializer):
    language_is_rtl = serializers.SerializerMethodField()
    
    class Meta:
        model = PhraseTranslation
        fields = ['uuid', 'phrase', 'text', 'language', 'language_is_rtl']
        read_only_fields = ['creator', 'uuid']
    
    def get_language_is_rtl(self, obj):
        code = (obj.language or '').strip().lower()
        base = code.split('-')[0]
        return code in RTL_LANGUAGE_CODES or base in RTL_LANGUAGE_CODES
        
    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user
        return super().create(validated_data)
    

class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = ['uuid', 'phrase']
        read_only_fields = ['creator', 'uuid']

    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user
        return super().create(validated_data)

class PhraseModifySerializer(serializers.Serializer):
    phrases = serializers.DictField(child=serializers.CharField(), required=True)

    def validate(self, attrs):
        request = self.context.get('request')
        language = None
        if request:
            language = request.query_params.get('language')
        if not language:
            raise serializers.ValidationError({"language": "This query parameter is required."})
        return attrs

    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user
        return super().create(validated_data)

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'uuid',
            'resource_controller',
            'resource_action',
            'resource_uuid',
            'status',
            'description',
            'message',
            'message_type',
            'created_at',
        ]