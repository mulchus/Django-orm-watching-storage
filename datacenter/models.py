from django.db import models
from django.utils.timezone import localtime, now
from datetime import timedelta
import re


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    
    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    
    def is_long(self, minutes=60):
        return self.get_duration() > timedelta(minutes=minutes)

    
    def get_duration(self):
        return localtime(self.leaved_at) - localtime(self.entered_at)
        
       
    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def format_duration(duration): 
    duration_stamp = (str(duration).split(".")[0]).split(":")
    if duration < timedelta(days=1):
        return f'{duration_stamp[0]}ч {duration_stamp[1]}мин'
    else:
        duration_stamp = re.split(' day, |:',str(duration))
        return f'{duration_stamp[0]}дн {duration_stamp[1]}ч {duration_stamp[2]}мин'
       