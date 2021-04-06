from django.db import models

# Create your models here.
class navbar(models.Model):
    page1 = models.CharField(max_length=100, blank=True, null=True)
    page2 = models.CharField(max_length=100, blank=True, null=True)
    page2 = models.CharField(max_length=100, blank=True, null=True)
    page3 = models.CharField(max_length=100, blank=True, null=True)
    page4 = models.CharField(max_length=100, blank=True, null=True)
    page5 = models.CharField(max_length=100, blank=True, null=True)
    page6 = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.page1