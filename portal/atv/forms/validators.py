from django.utils.deconstruct import deconstructible
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def PasswordValidator(value):
    validate_password(value)


def EmailInUseValidator(value):
    if User.objects.filter(email=value).first():
        raise ValidationError('Email já está em uso')
