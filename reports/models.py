import datetime
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.name


class TimeEntryManager(models.Manager):
    def for_month(self, year, month_no):
        return TimeEntry.objects.filter(date__month=month_no, date__year=year)

    def for_week(self, year, week_no):
        from isoweek import Week
        week = Week(year, week_no)
        return TimeEntry.objects.filter(date__gte=week.monday(), date__lte=week.sunday())


class TimeEntry(models.Model):
    objects = TimeEntryManager()

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
