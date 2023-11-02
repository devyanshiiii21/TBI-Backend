from .models import *
from rest_framework import serializers

class NidhiEirSerializer(serializers.ModelSerializer):
    class Meta:
        model = NidhiEIR
        fields = '__all__'

class NidhiPrayasSerializer(serializers.ModelSerializer):
    class Meta:
        model = NidhiPrayas
        fields = '__all__'

class TideEirSerializer(serializers.ModelSerializer):
    class Meta:
        model = TideEIR
        fields = '__all__'

class TideGrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = TideGrant
        fields = '__all__'