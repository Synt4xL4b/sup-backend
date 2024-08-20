from django.db import models
from django.utils import timezone
from ..users.models import User


class Category(models.Model):
    """
    Модель категория митов
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Meet(models.Model):
    """
    Модель самих митов, связана с категорией
    """
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    title = models.CharField(max_length=20, verbose_name="Название")
    start_date = models.DateField(default=timezone.now, verbose_name="Дата")
    start_time = models.TimeField(default=timezone.now, verbose_name="Время")

    def __str__(self):
        return f"{self.title} - {self.start_date} {self.start_time}"

    class Meta:
        verbose_name = 'Мит'
        verbose_name_plural = 'Миты'
        ordering = ['start_date', 'start_time', 'title']


class MeetParticipant(models.Model):
    """
    Модель участников митов и статусов
    """
    STATUS_CHOICES = [
        ('present', 'Присутствует'),
        ('absent', 'Отсутствует'),
        ('warned', 'Предупредил'),
    ]

    meet = models.ForeignKey(Meet, on_delete=models.PROTECT, verbose_name="Мит")
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь")

    def __str__(self):
        return f"{self.user.username} - {self.status} на {self.meet.title}"

    class Meta:
        verbose_name = 'Участник мита'
        verbose_name_plural = 'Участники мита'
        ordering = ['meet', 'user']




