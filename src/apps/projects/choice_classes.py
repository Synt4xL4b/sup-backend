from django.db import models


class ProjectChoices(models.TextChoices):
    DISCUSSION = "В обсуждении", "В обсуждении"
    DEVELOPMENT = "В разработке", "В разработке"
    SUPPORT = "В поддержке", "В поддержке"


class FeatureChoices(models.TextChoices):
    NEW = "Новая", "Новая"
    DEVELOPMENT = "Разработка", "Разработка"
    TESTING = "Тестирование", "Тестирование"
    SUCCESS = "Готов", "Готов"


class TaskChoices(models.TextChoices):
    NEW = "Новая", "Новая"
    DEVELOPMENT = "Разработка", "Разработка"
    TESTING = "Тестирование", "Тестирование"
    SUCCESS = "Готов", "Готов"
    BACKLOG = "Бэклог", "Бэклог"
