from django.db import models
from django.utils.translation import gettext_lazy as _

class DataPoint(models.Model):
    end_year = models.TextField(null=True,blank=True)
    intensity = models.TextField(null=True,blank=True)
    sector = models.TextField(null=True,blank=True)
    topic = models.TextField(null=True,blank=True)
    insight = models.TextField(null=True,blank=True)
    url = models.TextField(null=True,blank=True)
    region = models.TextField(max_length=100,null=True,blank=True)
    start_year = models.TextField(null=True,blank=True)
    impact = models.TextField(null=True,blank=True)
    added = models.TextField(null=True,blank=True)
    published = models.TextField(null=True,blank=True)
    country = models.TextField(null=True,blank=True)
    relevance = models.TextField(null=True,blank=True)
    pestle = models.TextField(null=True,blank=True)
    source = models.TextField(null=True,blank=True)
    title = models.TextField(null=True,blank=True)
    likelihood = models.TextField(null=True,blank=True)

    class Meta:
        db_table = 'datapoint'
        verbose_name = _('datapoint')
        verbose_name_plural = _('datapoints')


    def __str__(self):
        return f"DataPoint {self.id}"
