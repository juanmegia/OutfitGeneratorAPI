from rest_framework import serializers
from models import Piece
from models import PieceCategory
from models import Outfit
class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piece
        fields = ['id', 'name', 'code', 'category', 'description', 'image' ]

            
