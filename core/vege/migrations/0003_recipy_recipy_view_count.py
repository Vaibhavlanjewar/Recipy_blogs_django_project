# Generated by Django 5.0.7 on 2024-07-26 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_recipy_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipy',
            name='recipy_view_count',
            field=models.IntegerField(default=1),
        ),
    ]