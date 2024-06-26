# Generated by Django 5.0.6 on 2024-05-18 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OutfitGeneratorAPI', '0002_alter_piece_user_alter_outfit_user_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outfit',
            name='code',
        ),
        migrations.RemoveField(
            model_name='piece',
            name='code',
        ),
        migrations.RemoveField(
            model_name='piececategory',
            name='code',
        ),
        migrations.AlterField(
            model_name='piece',
            name='brand',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='piece',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='OutfitGeneratorAPI.piececategory'),
        ),
        migrations.AlterField(
            model_name='piece',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='piece',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='piece',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='piece',
            name='size',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='piece',
            name='style',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
