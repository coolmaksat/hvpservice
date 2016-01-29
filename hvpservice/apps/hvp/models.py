from __future__ import unicode_literals

from django.db import models


class Query(models.Model):

    vcf_file = models.FileField(upload_to='vcfs/%Y/%m/%d/')
    disease = models.CharField(max_length=64)


class Result(models.Model):
    pass
