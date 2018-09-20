from rest_framework import serializers
from .models import Subject, Card

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:

        model = Subject
        fields = '__all__'



class CardSerializer(serializers.ModelSerializer):

    class Meta:

        model = Card
        fields = '__all__'