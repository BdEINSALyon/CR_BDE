from django.db import models
import uuid
import os
from CR_BDE import settings


def random_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('', filename)


class Type(models.Model):
    name = models.CharField(max_length=30, verbose_name="Type de réunion")

    def __str__(self):
        return self.name


class Year(models.Model):
    name = models.CharField(max_length=30, verbose_name="Date du mandat", help_text="Exemple : 2018/2019")
    upload_active = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.name


class Report(models.Model):
    date = models.DateField(verbose_name="Date de la réunion", null=False, blank=False)
    file = models.FileField(verbose_name="Fichier CR", null=False, blank=False, upload_to=random_file_name)
    type = models.ForeignKey(verbose_name="Type de réunion", to=Type, null=False, blank=False, on_delete=models.PROTECT)
    year = models.ForeignKey(verbose_name="Mandat", to=Year, null=False, blank=False, on_delete=models.PROTECT)
    created_date = models.DateField(auto_now_add=True)
    download_number = models.IntegerField(default=0)
    is_public = models.BooleanField(default=True, null=False)

    def __str__(self):
        return "CR " + self.type.name + " du " + str(self.date)

    @property
    def get_url(self):
        return settings.MEDIA_ROOT + "/" + str(self.file)
