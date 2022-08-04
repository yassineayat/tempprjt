from django.db import models
from django.core.mail import send_mail
# Create your models here.
class opensnz(models.Model):
    temp = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.temp)

    def save(self, *args, **kwargs):
        if self.temp > 13:
            send_mail(
                'température dépasse la normale,' + str(self.temp),
                'anomalie dans la machine le,' + str(self.dt),
                'yassine.ayat@ump.ac.ma',
                ['yassine1960ayat@gmail.com'],
                fail_silently=False,
            )
        return super().save(*args, **kwargs)
