from django.utils.functional import cached_property
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from base.utils import LIST_OF_COUNTY, TRUE_OR_FALSE_CHOICES
from base.models_fields import CPFField, CNPJField, CEPField, PhoneField


class Person(BaseModel):
    GENDER_CHOICES = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('O', 'Outro')
    ]

    full_name = models.CharField(max_length=150, verbose_name='Nome Completo')

    birth_date = models.DateField(blank=True, null=True, verbose_name='Data de nascimento')

    cpf = CPFField(verbose_name='CPF')

    email = models.EmailField(max_length=100, blank=True, verbose_name='E-mail')

    phone = PhoneField(blank=True, null=True, verbose_name='Telefone')

    gender = models.CharField(max_length=15, verbose_name='Genero',
                              choices=GENDER_CHOICES,
                              blank=True, null=True)

    address = models.CharField(max_length=150, blank=True, null=True)

    city = models.ForeignKey(to=City, verbose_name='Município',
                             on_delete=models.PROTECT, null=True,
                             blank=True)

    state = models.CharField(max_length=20, blank=True,
                             null=True, verbose_name='UF',
                             choices=LIST_OF_COUNTY)

    cep = CEPField(max_length=9, blank=True, verbose_name='CEP')

    is_active = models.BooleanField(db_index=True, default=True,
                                    choices=TRUE_OR_FALSE_CHOICES,
                                    verbose_name='Ativo?')


class Company(BaseModel):
    cnpj = CNPJField(verbose_name='CNPJ', blank=True, null=True)

    business_name = models.CharField(max_length=100, verbose_name='Nome Fantasia')

    legal_name = models.CharField(max_length=100, verbose_name='Razão Social')

    email = models.EmailField(max_length=100, blank=True, verbose_name='E-mail')

    address = models.CharField(max_length=150, blank=True, null=True)

    city = models.ForeignKey(to=City, verbose_name='Município',
                             on_delete=models.PROTECT, null=True, blank=True)

    state = models.CharField(max_length=20, blank=True, null=True,
                             verbose_name='UF', choices=LIST_OF_COUNTY)

    cep = CEPField(null=True, blank=True, verbose_name='CEP')

    phone = PhoneField(null=True, blank=True, verbose_name='Telefone')

    fax = models.CharField(max_length=100, blank=True, verbose_name='Fax')

    site = models.URLField(max_length=100, blank=True, verbose_name='Site')

    is_active = models.BooleanField(db_index=True, default=True,
                                    choices=TRUE_OR_FALSE_CHOICES, verbose_name='Ativo?')

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.business_name
