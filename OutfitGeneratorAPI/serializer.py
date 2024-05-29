from rest_framework import serializers
from OutfitGeneratorAPI.models import Piece
from OutfitGeneratorAPI.models import Outfit
from django.contrib.auth.models import User
class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piece
        fields = '__all__'
class OutfitSerializer(serializers.ModelSerializer):
    pieces = PieceSerializer(many=True)

    class Meta:
        model = Outfit
        fields = ['id', 'name', 'pieces']

    def create(self, validated_data):
        pieces_data = validated_data.pop('pieces')
        outfit = Outfit.objects.create(**validated_data)
        for piece_data in pieces_data:
            Piece.objects.create(outfit=outfit, **piece_data)
        return outfit
            
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user