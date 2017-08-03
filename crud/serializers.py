from rest_framework import serializers
from .models import Crudlist

class CrudlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crudlist
        fields = ('id', 'title', 'description', 'completed', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
