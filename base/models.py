import re
import random
import time

from uuid import uuid4
from typing import TYPE_CHECKING

from django.utils.functional import cached_property
from django.db import models
# from django.utils.translation import ugettext_lazy as _
from base.utils import LIST_OF_COUNTY, TRUE_OR_FALSE_CHOICES
from base.models_fields import CPFField, CNPJField, CEPField, PhoneField

if TYPE_CHECKING:
    from uuid import UUID

    from typing import Optional
    from typing_extensions import Self

    from django.db.models import Manager


class BaseHelperModel:
    def __init__(self, instance) -> None:
        self._instance = instance

    @property
    def instance(self):
        return self._instance


class BaseModel(models.Model):
    """ Classe que cria os fields básicos de outros models """
    unique_id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        unique=True
    )

    created = models.DateTimeField(
        verbose_name='Criado em',
        auto_now_add=True,
        editable=False
    )

    modified = models.DateTimeField(
        verbose_name='Atualizado em',
        auto_now=True,
        editable=False
    )

    class_utils = BaseHelperModel

    objects: "Manager[Self]"
    pk: "Optional[UUID]"

    class Meta:
        abstract = True

    @cached_property
    def utils(self) -> "class_utils":
        return self.class_utils(self)

    @classmethod
    def get_verbose_name(cls):
        return cls._meta.verbose_name

    @classmethod
    def get_verbose_name_plural(cls):
        return cls._meta.verbose_name_plural

    @classmethod
    def get_or_none(cls, **kwargs) -> "Optional[Self]":
        try:
            return cls.objects.get(**kwargs)
        except cls.DoesNotExist:
            return None


class City(BaseModel):
    """ lista de municípios do sistema """
    uf = models.CharField(verbose_name='UF', max_length=2,
                          null=True, blank=True)

    name = models.CharField(verbose_name='Município', max_length=80,
                            null=True, blank=True)

    geoIBGEId = models.CharField(verbose_name='IBGE', max_length=7,
                                 null=True, blank=True)

    def __str__(self):
        return str(self.name)

    @classmethod
    def choices(cls):
        """ retorna todos os municípios do sistema """
        return [(None, '-------------'), ] + list(
            cls.objects.all().values_list('pk', 'name'))

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municípios'
        ordering = ['uf', 'name']


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
