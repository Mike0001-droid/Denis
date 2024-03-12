# Generated by Django 5.0.2 on 2024-03-05 04:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsapp', '0002_remove_hockeyplayer_team_hockeyplayer_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rodkom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя родкома')),
                ('last_name', models.CharField(max_length=50, null=True, verbose_name='Фамилия родкома')),
                ('otchevstvo', models.CharField(max_length=50, null=True, verbose_name='Отчество родкома')),
                ('phone', models.CharField(max_length=11, verbose_name='Номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='Trener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя тренера')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия тренера')),
                ('otchevstvo', models.CharField(max_length=50, verbose_name='Отчество тренера')),
                ('phone', models.CharField(max_length=11, verbose_name='Номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('an', models.IntegerField(verbose_name='Удаленность от катка Апрелевка')),
                ('year', models.IntegerField(verbose_name='Год рождения игроков')),
                ('uroven', models.CharField(max_length=100, verbose_name='Уровень')),
                ('team', models.CharField(max_length=100, verbose_name='Команда')),
                ('turnir', models.CharField(max_length=20, verbose_name='Дата турнира')),
                ('status', models.CharField(choices=[('Нет', 'Нет'), ('Думают', 'Думают'), ('Будут', 'Будут'), ('Жду', 'Жду'), ('Гарантия', 'Гарантия')], max_length=8, null=True, verbose_name='Ответ')),
                ('data', models.DateTimeField(verbose_name='Дата последнего сообщения')),
                ('zametki', models.CharField(max_length=255, verbose_name='Заметки')),
                ('vazhno', models.CharField(max_length=255, verbose_name='Важно')),
                ('rodkom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rodkom', to='whatsapp.rodkom')),
                ('trener', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trener', to='whatsapp.trener')),
            ],
        ),
        migrations.DeleteModel(
            name='HockeyPlayer',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
