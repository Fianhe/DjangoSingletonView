from rest_framework import viewsets
from example.models import SingletonModel
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from django import shortcuts

class SingletonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingletonModel


class SingletonView(viewsets.ModelViewSet):

    serializer_class = SingletonSerializer

    def get_queryset(self):
        return SingletonModel.objects.all()[:1]

    def create(self, request, *args, **kwargs):
        if not self.get_queryset().exists():
            return super(SingletonView, self).create(request, *args, **kwargs)
        else:
            return Response({
                'message': 'Already exists and can be only one!'
            }, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = shortcuts.get_object_or_404(queryset)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj


