from django.db import models

class Registration(models.Model):
    device_library_identifier = models.CharField(max_length=50)
    pass_type_identifier = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    push_token = models.CharField(max_length=50)

    def __unicode__(self):
        return self.device_library_identifier
