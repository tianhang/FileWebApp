from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from datetime import datetime
from django.utils import timezone

import uuid,os
# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


# Create your models here.

class TimeStampModel(models.Model):
    #created_date = models.DateTimeField(default=timezone.now(), blank=True)
    created_date = models.DateTimeField(auto_now_add=True,blank=True)
    class Meta:
        abstract = True

# generating unique id for each file
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('files', filename)

#file model
class File(TimeStampModel):
    filename_text = models.CharField(max_length=20)
    description_text = models.CharField(max_length=200)
    file = models.FileField(upload_to=get_file_path)

    def __str__(self):
        return self.filename_text

# receive the pre_delete signal and call the delete method on the FileField object
@receiver(pre_delete, sender=File)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.file.delete(False)


class FileAdmin(admin.ModelAdmin):
    list_display = ('filename_text','created_date')

admin.site.register(File,FileAdmin)



