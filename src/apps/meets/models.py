from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

from apps.users.models import User
from apps.meets.choice_classes import StatusChoice


class Category(models.Model):
    """
    Модель категория митов
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="Категория")

    class Meta:
        db_table = "category"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Meet(models.Model):
    """
    Модель самих митов, связана с категорией
    """
    category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Категория")
    title = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Название",
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Zа-яА-Я\s]*$",
                message="Допускаются только буквы латиницы и кириллицы.",
                code="invalid_name"
            ),
        ],
    )
    start_date = models.DateField(default=timezone.now, verbose_name="Дата")
    start_time = models.TimeField(default=timezone.now, verbose_name="Время")
    participant = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Участник")
    status = models.CharField(max_length=10, choices=StatusChoice.choices, default=StatusChoice.PRESENT, verbose_name="Статус")

    @property
    def status_color(self):
        return StatusChoice.get_color(self.status)

    class Meta:
        db_table = "meets"
        verbose_name = "Мит"
        ordering = ["start_date", "start_time", "title"]
        verbose_name_plural = "Миты"

    def __str__(self):
        return f"{self.title} - {self.start_date} {self.start_time}"






