from django.db import models


class StatusChoice(models.TextChoices):
    PRESENT = "present", "Присутствует"
    ABSENT = "absent", "Отсутствует"
    WARNED = "warned", "Предупредил"

    @classmethod
    def get_color(cls, status):
        if status == cls.PRESENT:
            return "green"
        elif status == cls.ABSENT:
            return "red"
        elif status == cls.WARNED:
            return "yellow"
        return "grey"
