# Generated by Django 5.0.2 on 2024-03-05 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsapp', '0004_alter_contact_rodkom_alter_contact_trener'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='status',
            field=models.CharField(blank=True, choices=[('Нет', 'Нет'), ('Думают', 'Думают'), ('Будут', 'Будут'), ('Жду', 'Жду'), ('Гарантия', 'Гарантия')], max_length=8, null=True, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='vazhno',
            field=models.CharField(blank=True, max_length=255, verbose_name='Важно'),
        ),
    ]
