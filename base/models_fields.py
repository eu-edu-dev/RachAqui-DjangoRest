from django.db import models

from base.utils import validate_cpf, validate_cnpj, validate_cep, validate_phone


class CPFField(models.CharField):
    default_validators = [validate_cpf]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 11
        super().__init__(*args, **kwargs)


class CNPJField(models.CharField):
    default_validators = [validate_cnpj]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 14
        super().__init__(*args, **kwargs)


class CEPField(models.CharField):
    default_validators = [validate_cep]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 8
        super().__init__(*args, **kwargs)


class PhoneField(models.CharField):
    default_validators = [validate_phone]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        super().__init__(*args, **kwargs)
