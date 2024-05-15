import uuid

from django.db import models

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
class Piece(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    brand = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    size = models.CharField(max_length=3)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name + ' - ' + self.brand + ' - ' + self.category

class PieceCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    bodypart = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Outfit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    pieces = models.ManyToManyField(Piece)


    def __str__(self):
        return self.name