# Generated by Django 5.1.3 on 2024-11-18 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
