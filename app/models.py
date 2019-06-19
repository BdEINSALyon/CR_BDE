from django.db import models
from CR_BDE import settings


class Type(models.Model):
    name = models.CharField(max_length=30, verbose_name="Type de réunion")

    def __str__(self):
        return self.name

    @property
    def count_report_byyear(self, year):
        return Report.objects.filter(is_public=True).filter(year=year).filter(type=self).count()


class Year(models.Model):
    name = models.CharField(max_length=30, verbose_name="Date du mandat", help_text="Exemple : 2018/2019")
    upload_active = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.name

    @property
    def count_report(self):
        return Report.objects.filter(is_public=True).filter(year=self).count()


class Report(models.Model):
    date = models.DateField(verbose_name="Date de la réunion", null=False, blank=False)
    file = models.FileField(verbose_name="Fichier CR", null=False, blank=False)
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
