from rest_framework import serializers 
from .models import ReadingMemo 

class ReadingMemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingMemo
        fields = '__all__'

        