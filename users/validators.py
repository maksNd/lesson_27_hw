from datetime import date

from rest_framework.exceptions import ValidationError


def check_birth_date(value):
    age = date.today().year - value.year
    if age < 9:
        raise ValidationError('Нельзя регистрировать пользователей моложе 9ти ллет')


def check_email(value):
    if 'rambler' in value:
        raise ValidationError('Регистрация с домена rambler запрещена')


