# Generated by Django 4.0.3 on 2022-08-21 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeboxapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Recipe',
        ),
        migrations.AlterField(
            model_name='author',
            name='byline',
            field=models.CharField(max_length=100),
        ),
    ]
