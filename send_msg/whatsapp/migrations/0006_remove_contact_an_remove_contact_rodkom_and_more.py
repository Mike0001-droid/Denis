# Generated by Django 5.0.2 on 2024-03-05 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsapp', '0005_alter_contact_status_alter_contact_vazhno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='an',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='rodkom',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='team',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='trener',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='uroven',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='year',
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=100, verbose_name='Команда')),
                ('year', models.IntegerField(verbose_name='Год рождения игроков')),
                ('uroven', models.CharField(max_length=100, verbose_name='Уровень')),
                ('an', models.IntegerField(verbose_name='Удаленность от катка Апрелевка')),
                ('rodkom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rodkom', to='whatsapp.rodkom')),
                ('trener', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trener', to='whatsapp.trener')),
            ],
        ),
    ]
