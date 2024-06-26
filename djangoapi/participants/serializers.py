from rest_framework import serializers
from .models import Participant

# From Here you create your API by calling the model you wrote.
class ParticipantSerializers(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('id','name','email','phone')
