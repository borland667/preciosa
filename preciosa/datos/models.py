# -*- coding: utf-8 -*-
from django.db import models
from model_utils import Choices


class IdProductoOnline(models.Model):
    """Se conocen descripciones de los productos,
       pero no su identificador unívoco que es el UPC.

       https://github.com/mgaitan/preciosa/issues/146
       """

    sucursal = models.ForeignKey('precios.Sucursal',
                                 limit_choices_to={'onlinel': True})
    producto = models.ForeignKey('precios.Producto')
    id_online = models.CharField(max_length=100,
                                 help_text=u"algun identificador unico del "
                                           u"producto en el sitio online. Ejemplo el PLU "
                                           u"de Cotodigital")
    url = models.URLField(max_length=200,
                          null=True, blank=True,
                          help_text=u"Url al detalle del producto en la "
                                    u"sucursal, si existe")



class SucursalMapper(models.Model):
    """
    Un modelo para mapear sucursales, por ejemplo, para ser utilizado por importaderos de datos.
    """
    class Meta:
        unique_together = [('source', 'id_source')]

    SOURCES = Choices('preciosclaros',)
    source = models.CharField(max_length=20, choices=SOURCES)
    id_source = models.CharField(max_length=20)
    sucursal = models.ForeignKey('precios.Sucursal')

