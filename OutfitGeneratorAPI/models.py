import uuid

from django.db import models
from django.contrib.auth.models import User

class PieceCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    bodypart = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Piece(models.Model):
    STYLE_CHOICES = [
        ('CASUAL', 'Casual'),
        ('FORMAL', 'Formal'),
        ('SPORT', 'Sport'),
        ('BUSINESS', 'Business'),
    ]
    COLOR_CHOICES = (
        ('RED', 'Red'),
        ('GREEN', 'Green'),
        ('BLUE', 'Blue'),
        ('YELLOW', 'Yellow'),
        ('BLACK', 'Black'),
        ('WHITE', 'White'),
        ('ORANGE', 'Orange'),
        ('PURPLE', 'Purple'),
        ('PINK', 'Pink'),
        ('BROWN', 'Brown'),
        ('GRAY', 'Gray'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100,blank=True)
    name = models.CharField(max_length=100,blank=True, null= True)
    brand = models.CharField(max_length=100,blank=True, null= True)
    style = models.CharField(max_length=100,choices=STYLE_CHOICES, null =True)
    color = models.CharField(max_length=100,choices=COLOR_CHOICES, null= True)
    category = models.ForeignKey(PieceCategory, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True, null= True)
    size = models.CharField(max_length=3,blank=True, null= True)
    image = models.ImageField(upload_to='images/',blank=True, null= True)

    def __str__(self):
        return f"{self.name} - {self.brand} - {self.get_style_display()} - {str(self.category)}"

class Outfit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pieces = models.ManyToManyField(Piece)


    def __str__(self):
        return self.name