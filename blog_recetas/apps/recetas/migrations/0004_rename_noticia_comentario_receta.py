# Generated by Django 4.2.7 on 2023-12-30 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0003_receta_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='noticia',
            new_name='receta',
        ),
    ]
