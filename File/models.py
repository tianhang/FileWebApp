from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from datetime import datetime

# Create your models here.

class TimeStampModel(models.Model):
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        abstract = True

class File(TimeStampModel):
    filename_text = models.CharField(max_length=20)
    description_text = models.CharField(max_length=200)
    file = models.FileField(upload_to="files")

    def __str__(self):
        return self.filename_text

    def __unicode__(self):
        return unicode(self.file)

class FileAdmin(admin.ModelAdmin):
    list_display = ('filename_text','created_date')

admin.site.register(File,FileAdmin)



