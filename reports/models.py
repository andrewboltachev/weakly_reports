import datetime
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.name


class TimeEntry(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=1024, blank=True)
    time = models.DecimalField(max_digits=3, decimal_places=1)
    date = models.DateField(default=datetime.date.today)

    def __unicode__(self):
        return '%s - %sh on %s' % (
            self.project.name,
            str(self.time),
            self.date.strftime('%Y-%m-%d')
        )
    
    class Meta:
        ordering = ['date', 'id']
