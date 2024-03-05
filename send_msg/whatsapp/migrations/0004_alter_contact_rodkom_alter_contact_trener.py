# Generated by Django 5.0.2 on 2024-03-05 04:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsapp', '0003_rodkom_trener_contact_delete_hockeyplayer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='rodkom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rodkom', to='whatsapp.rodkom'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='trener',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trener', to='whatsapp.trener'),
        ),
    ]