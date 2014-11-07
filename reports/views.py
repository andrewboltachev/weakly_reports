from django.shortcuts import render
from htmler.bootstrap import bootstrap3, container
from htmler.fun import ul, li, div, h2, h4, a
from htmler.tags import SafeString
from django.http import HttpResponse
from .models import Project, TimeEntry
from django.core.urlresolvers import reverse


def home(request):
    data = [
        (2014, [45, 46], [10, 11]),
    ]
    h_year = lambda year, weeks, months: div(h2(str(year)), weeks, months)
    h_weeks_for_year = lambda *x: div(h4('Weeks'), ul(*x))
    h_months_for_year = lambda *x: div(h4('Months'), ul(*x))
    h_week = lambda m, y: li(a(str(m), href=reverse('weekly', kwargs={'year':y, 'week_no':m})))
    h_month = lambda w, y : li(a(str(w), href=reverse('monthly', kwargs={'year':y, 'month_no':w})))
    contents = [
        h_year(y,
            h_weeks_for_year(*[h_week(w, y) for w in b]),
            h_months_for_year(*[h_month(m, y) for m in c])
        )
        for y, b, c in data
    ]
    html = bootstrap3(container(*contents))
    return HttpResponse(html)


def weekly(request, year, week_no):
    return HttpResponse(html)


def monthly(request, year, week_no):
    pass
