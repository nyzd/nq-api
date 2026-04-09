from rest_framework import permissions, viewsets, status, filters, serializers
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from core import permissions as core_permissions
from core.pagination import CustomLimitOffsetPagination
from quran.models import Provenance
from quran.serializers import ProvenanceSerializer, ProvenanceAddSerializer
from django.db.models import Q

class ProvenanceViewSet(viewsets.ModelViewSet):
    queryset = Provenance.objects.filter(~Q(child_provenance=None) & Q(parent_provenance=None))
    serializer_class = ProvenanceSerializer
    permission_classes = [
        core_permissions.IsCreatorOrReadOnly,
        # core_permissions.IsCreatorOfParentOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly | permissions.DjangoModelPermissions
    ]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["role"]
    ordering_fields = ['created_at']
    pagination_class = CustomLimitOffsetPagination
    lookup_field = "uuid"

    def get_serializer_class(self):
        if self.action == 'create':
            return ProvenanceAddSerializer
        return ProvenanceSerializer

