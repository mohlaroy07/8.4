from rest_framework import serializers
from .models import Klass, Mehmonxona, Travel


class KlassSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Klass
        fields = '__all__'
        
        
class MehmonxonaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mehmonxona
        fields = '__all__'
        
                
class TravelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Travel
        fields = '__all__'        