from django.http import JsonResponse
from OutfitGeneratorAPI.models import Piece, Outfit, User
from OutfitGeneratorAPI.serializer import PieceSerializer, OutfitSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from random import sample


@api_view(['GET', 'POST'])
def piece_list(request):
    if request.method == 'GET':
        user_id = request.query_params.get('user_id', None)
        if user_id:
            pieces = Piece.objects.filter(user_id=user_id)
        else:
            pieces = Piece.objects.all()
        serializer = PieceSerializer(pieces, many=True)
        return JsonResponse({"pieces": serializer.data})
    if request.method == 'POST':
        serializer = PieceSerializer(data=request.data)
        if serializer.is_valid():
            user_id = request.data.get('user_id')  # Assuming user_id is passed in request data
            user = User.objects.get(pk=user_id)
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def piece_detail(request, id):
    try:
        piece = Piece.objects.get(pk=id)
    except Piece.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PieceSerializer(piece)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PieceSerializer(piece, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        piece.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def piece_category(request):
    category = request.query_params.get('category', None)
    color = request.query_params.get('color', None)
    size = request.query_params.get('size', None)
    user_id = request.query_params.get('user_id', None)

    filters = {}
    if category:
        filters['category'] = category
    if color:
        filters['color'] = color
    if size:
        filters['size'] = size
    if user_id:
        filters['user_id'] = user_id

    try:
        pieces = Piece.objects.filter(**filters)
    except Piece.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PieceSerializer(pieces, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def outfit_list(request):
    user_id = request.query_params.get('user_id', None)
    if user_id:
        outfits = Outfit.objects.filter(user_id=user_id)
        serializer = OutfitSerializer(outfits, many=True)
        return JsonResponse({"outfits": serializer.data})
    else:
        return Response({"message": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_outfit(request):
        serializer = OutfitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_outfit(request, outfit_id):
        try:
            outfit = Outfit.objects.get(pk=outfit_id)
        except Outfit.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = OutfitSerializer(outfit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def generate_outfit_view(request):
    # Obtener parámetros de la solicitud
    user_id = request.GET.get('user_id')
    selected_style = request.GET.get('style')
    selected_weather = request.GET.get('weather')
    selected_categories = request.GET.getlist('categories')

    # Validar que se proporcionen todos los parámetros necesarios
    if not user_id or not selected_categories:
        return JsonResponse({"error": "Se requieren user_id y categories"}, status=400)

    # Generar el outfit
    outfit = generate_outfit(user_id, selected_style, selected_weather, selected_categories)

    if outfit:
        return JsonResponse({"outfit": outfit})
    else:
        return JsonResponse({"error": "No se pudieron encontrar suficientes piezas para generar un outfit"}, status=404)
def generate_outfit(user_id, selected_style=None, selected_weather=None, selected_categories=None):
    # Obtener todas las piezas del usuario
    user_pieces = Piece.objects.filter(user_id=user_id)

    # Filtrar piezas basadas en el estilo seleccionado
    if selected_style:
        user_pieces = user_pieces.filter(style=selected_style)

    # Filtrar piezas basadas en el clima seleccionado
    if selected_weather:
        user_pieces = user_pieces.filter(weather=selected_weather)

    # Filtrar piezas basadas en las categorías seleccionadas
    if selected_categories:
        user_pieces = user_pieces.filter(category__in=selected_categories)

    # Seleccionar una pieza de cada categoría
    selected_pieces = {}
    for category in selected_categories:
        pieces_in_category = user_pieces.filter(category=category)
        if pieces_in_category.exists():
            selected_pieces[category] = sample(list(pieces_in_category), 1)[0]

    # Verificar si hay suficientes piezas para generar un outfit
    if len(selected_pieces) < 3:
        return None  # No hay suficientes piezas para generar un outfit

    outfit = {
        "top": selected_pieces.get("top"),
        "bottom": selected_pieces.get("bottom"),
        "footwear": selected_pieces.get("footwear"),
        "weather": selected_weather,
        "style": selected_style
    }
    outfit_json = json.dumps(outfit)

    return outfit_json