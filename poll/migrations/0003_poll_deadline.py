# Generated by Django 3.0.5 on 2024-04-10 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
