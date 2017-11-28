from rest_framework import serializers
from nature_cards_rest.models import NatureCard, NatureImage
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class NatureCardSerializer(serializers.ModelSerializer):
    #related_images = serializers.PrimaryKeyRelatedField(many=True, queryset=NatureImage.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = NatureCard
        fields = ('pk', 'name', 'description', 'created', 'owner', ) 

class NatureImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NatureImage
        fields = ('pk', 'image', 'thumbnail', 'title', 'description', 'created', 'card', )