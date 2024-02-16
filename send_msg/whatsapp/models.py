from django.db import models

class BookOfPhone (models.Model):
    name = models.CharField('Имя человека', max_length=20)
    phone = models.IntegerField('Номер телефона')

    def __str__(self):
        return f"{self.pk}) {self.name} Номер: {self.phone}"
