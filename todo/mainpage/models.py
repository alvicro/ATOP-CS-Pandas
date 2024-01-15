from django.db import models
from datetime import datetime
# Описание таблицы для хранения информации,
# предполагая, что строка таблицы - это один
# объект некоторого класса
class Task(models.Model):
    start = models.DateTimeField(default=datetime.now)
    end = models.DateTimeField()
    description = models.CharField(max_length=256, default='')
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.description)  # + ',' + self.start.strftime('%Y-%m-%d %H:%M:%S')