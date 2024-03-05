from django.db import models

STATUS_CHOICES = (
    ('Нет', 'Нет'),
    ('Думают', 'Думают'),
    ('Будут', 'Будут'),
    ('Жду', 'Жду'),
    ('Гарантия', 'Гарантия'),
)


class Trener(models.Model):
    first_name = models.CharField('Имя тренера', max_length=50)
    last_name = models.CharField('Фамилия тренера', max_length=50)
    otchevstvo = models.CharField('Отчество тренера', max_length=50)
    phone = models.CharField('Номер телефона', max_length=11)
    def __str__(self):
        return f"{self.last_name}-{self.phone}"

class Rodkom(models.Model):
    first_name = models.CharField('Имя родкома', max_length=50)
    last_name = models.CharField('Фамилия родкома', max_length=50, null=True)
    otchevstvo = models.CharField('Отчество родкома', max_length=50, null=True)
    phone = models.CharField('Номер телефона', max_length=11)
    def __str__(self):
        return f"{self.first_name}-{self.phone}"

class Team(models.Model):
    team = models.CharField('Команда', max_length=100)
    year = models.IntegerField('Год рождения игроков')
    uroven = models.CharField('Уровень', max_length=100)
    rodkom = models.ForeignKey(Rodkom, on_delete=models.CASCADE, related_name='rodkom', null=True, blank=True)
    trener = models.ForeignKey(Trener, on_delete=models.CASCADE, related_name='trener', null=True, blank=True)
    an = models.IntegerField('Удаленность от катка Апрелевка')
    def __str__(self):
        return f"{self.team}"


class Contact(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teams', null=True, blank=True)
    turnir = models.CharField('Дата турнира', max_length=20)
    status = models.CharField('Ответ', max_length=8, choices=STATUS_CHOICES, null=True, blank=True) 
    data = models.DateTimeField('Дата последнего сообщения')
    zametki = models.CharField('Заметки', max_length=255)
    vazhno = models.CharField('Важно', max_length=255, blank=True)
