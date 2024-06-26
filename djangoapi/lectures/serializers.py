from rest_framework import serializers
from .models import lecture

# From Here you create your API by calling the model you wrote.
class LectureSerializers(serializers.ModelSerializer):
    class Meta:
        model = lecture
        fields = ('id','name','language','price')
