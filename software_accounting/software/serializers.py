from rest_framework import serializers
from .models import Software

class SoftwareSerializer(serializers.ModelSerializer):

    class Meta:
        model = Software 
        fields = (
            'id',
            'title',
            'price',
            'currency',
            'count',
        )