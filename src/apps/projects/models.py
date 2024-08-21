from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

User = get_user_model()


class Project(models.Model):
    """Модель проекты"""

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ["-name"]

    DISCUSSION = "В обсуждении"
    DEVELOPMENT = "В разработке"
    SUPPORT = "В поддержке"

    STATUS_CHOICES = [
        (DISCUSSION, "В обсуждении"),
        (DEVELOPMENT, "В разработке"),
        (SUPPORT, "В поддержке"),
    ]

    name = models.CharField(max_length=20, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="Ссылка")
    logo = models.ImageField(
        upload_to="project_logos",
        verbose_name="Логотип",
        blank=True,
        null=True,
    )
    description = models.TextField(
        max_length=500, verbose_name="Описание", blank=True, null=True
    )
    participants = models.ManyToManyField(
        to=User, related_name="project_participants"
    )
    responsible = models.ForeignKey(
        to=User,
        related_name="project_responsibles",
        on_delete=models.CASCADE,
        verbose_name="Ответственный",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=DISCUSSION,
        verbose_name="Статус",
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + "_" + str(self.pk)
        return super().save()


class Tags(models.Model):
    """Модель тегов"""

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    name = models.CharField(max_length=50, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="Ссылка")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + "_" + str(self.pk)
        return super().save()


class Feature(models.Model):
    """Модель фичи"""

    class Meta:
        verbose_name = "Фича"
        verbose_name_plural = "Фичи"

    NEW = "Новая"
    DEVELOPMENT = "Разработка"
    TESTING = "Тестирование"
    SUCCESS = "Готов"

    STATUS_CHOICES = [
        (NEW, "Новая"),
        (DEVELOPMENT, "Разработка"),
        (TESTING, "Тестирование"),
        (SUCCESS, "Готов"),
    ]

    name = models.CharField(max_length=50, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="Ссылка")
    description = models.TextField(max_length=10000, verbose_name="Описание")
    importance = models.PositiveIntegerField(
        default=0, verbose_name="Важность"
    )
    tags = models.ManyToManyField(
        to=Tags, related_name="feature_tags", verbose_name="Теги"
    )
    participants = models.ManyToManyField(
        to=User,
        related_name="feature_participants",
        verbose_name="Исполнители",
    )
    responsible = models.ForeignKey(
        to=User,
        related_name="feature_responsibles",
        on_delete=models.CASCADE,
        verbose_name="Ответственный",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=NEW,
        verbose_name="Статус",
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + "_" + str(self.pk)
        return super().save()


class Task(models.Model):
    """Модель задачи"""

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    NEW = "Новая"
    DEVELOPMENT = "Разработка"
    TESTING = "Тестирование"
    SUCCESS = "Готов"
    BACKLOG = "Бэклог"

    STATUS_CHOICES = [
        (NEW, "Новая"),
        (DEVELOPMENT, "Разработка"),
        (TESTING, "Тестирование"),
        (SUCCESS, "Готов"),
        (BACKLOG, "Бэклог"),
    ]

    name = models.CharField(max_length=50, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="Ссылка")
    description = models.TextField(max_length=10000, verbose_name="Описание")
    importance = models.PositiveIntegerField(
        default=0, verbose_name="Важность"
    )
    tags = models.ManyToManyField(
        to=Tags, related_name="task_tags", verbose_name="Теги"
    )
    participants = models.ManyToManyField(
        to=User, related_name="task_participants", verbose_name="Исполнители"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=NEW,
        verbose_name="Статус",
    )
    date_execution = models.DateField(verbose_name="Дата исполнения")
    feature = models.ForeignKey(
        to=Feature,
        related_name="task_feature",
        on_delete=models.CASCADE,
        verbose_name="Фича",
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + "_" + str(self.pk)
        return super().save()
