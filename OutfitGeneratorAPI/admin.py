from django.contrib import admin
from OutfitGeneratorAPI.models import Piece
from OutfitGeneratorAPI.models import Outfit
from OutfitGeneratorAPI.models import PieceCategory

admin.site.register(Piece)
admin.site.register(Outfit)
admin.site.register(PieceCategory)