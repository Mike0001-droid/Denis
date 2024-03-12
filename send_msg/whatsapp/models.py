from django.db import models
from datetime import datetime

STATUS_CHOICES = (
    ('Нет', 'Нет'),
    ('Думают', 'Думают'),
    ('Будут', 'Будут'),
    ('Жду', 'Жду'),
    ('Гарантия', 'Гарантия'),
)

REPRESENTATIVE_CHOICES = (
    ('Родком', 'Родком'),
    ('Тренер', 'Тренер'),
)

class Representative(models.Model):
    status = models.CharField('Статус представителя команды', choices=REPRESENTATIVE_CHOICES, max_length=6)  # тренер или родитель
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField('Фамилия', max_length=20, null=True, blank=True)
    surname = models.CharField('Отчество', max_length=20, null=True, blank=True)
    phone = models.IntegerField('Телефон')

    def __str__(self):
        return f'{self.last_name} + {self.first_name} + {self.phone}'

class Team(models.Model):
    name = models.CharField('Название', max_length=50, null=True)
    town = models.CharField('Город', max_length=50, null=True)
    represent = models.ForeignKey(Representative, on_delete=models.CASCADE, related_name='representative', null=True, blank=True)
    distance_to = models.CharField('до Апрелевки', max_length=50, null=True, blank=True)  # можно ли сделать так, чтобы расстояние считалось самостоятельно?
    year = models.IntegerField('Год рождения игроков')
    level = models.CharField('Уровень', max_length=10, null=True, blank=True)  # 1, 2, 3 или 4

    def __str__(self):
        return f'{self.name} + {self.year} + {self.level}'

class Status(models.Model):
    answer = models.CharField('Решение команды', choices=STATUS_CHOICES, max_length=8, null=True, blank=True)  # варианты: Жду, Думает, Будут, Гарантия, Нет
    comment = models.CharField('Комментарий', max_length=255, null=True, blank=True)
    last_message = models.DateTimeField('Дата последнего сообщения')

    def __str__(self):
        return f'{self.answer}'

class Tournament(models.Model):
    town = models.CharField('Город', max_length=50, default='Апрелевка')
    ice_rink = models.CharField('Название катка', max_length=50, default='April_ice')
    team = models.ManyToManyField(Team)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status', null=True, blank=True)
    data = models.DateField('Даты проведения')

    #TODO
    """ def data(self):
        dirname = datetime.now().strftime('%Y/%m/%d')
        return  """

    def __str__(self):
        return f'{self.ice_rink} + {self.data}'
