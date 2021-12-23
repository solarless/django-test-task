from rest_framework.serializers import ModelSerializer

from .models import Footballer


class FootballerSerializer(ModelSerializer):
    class Meta:
        model = Footballer
        fields = '__all__'
