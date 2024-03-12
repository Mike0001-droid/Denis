# Generated by Django 5.0.2 on 2024-03-05 04:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsapp', '0006_remove_contact_an_remove_contact_rodkom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='whatsapp.team'),
        ),
    ]
