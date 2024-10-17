from django.db import models

from core.models import BaseModel
# Create your models here.


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
