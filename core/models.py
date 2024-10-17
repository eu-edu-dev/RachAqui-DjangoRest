from uuid import uuid4
from typing import TYPE_CHECKING

from django.utils.functional import cached_property
from django.db import models

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
