from rest_framework import serializers
from OutfitGeneratorAPI.models import Piece
from OutfitGeneratorAPI.models import Outfit
class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piece
        fields = ['id', 'user','name', 'brand', 'style', 'category','size','description', 'image' ]
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
            
