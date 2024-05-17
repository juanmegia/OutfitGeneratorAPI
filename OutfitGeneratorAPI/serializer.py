from rest_framework import serializers
from OutfitGeneratorAPI.models import Piece
from OutfitGeneratorAPI.models import Outfit
class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piece
        fields = ['id', 'name', 'code', 'category', 'description', 'image' ]
class OutfitSerializer(serializers.ModelSerializer):
    pieces = PieceSerializer(many=True)

    class Meta:
        model = Outfit
        fields = ['id', 'name', 'code', 'pieces']

    def create(self, validated_data):
        pieces_data = validated_data.pop('pieces')
        outfit = Outfit.objects.create(**validated_data)
        for piece_data in pieces_data:
            Piece.objects.create(outfit=outfit, **piece_data)
        return outfit
            
