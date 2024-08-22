from django.core.validators import MaxValueValidator, RegexValidator


class LettersOnlyValidator:
    @staticmethod
    def get_regex_validator():
        return RegexValidator(
            regex=r"^[a-zA-Zа-яА-Я\s]*$",
            message="Допускаются только буквы латиницы и кириллицы.",
            code="invalid_name",
        )

    @staticmethod
    def get_max_value_validator():
        return MaxValueValidator(limit_value=1_000_000)
