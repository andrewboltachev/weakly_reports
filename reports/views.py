import datetime
import operator
import functools
from django.shortcuts import render
from htmler.bootstrap import bootstrap3, container
from htmler.fun import ul, li, div, h1, h2, h3, h4, a, strong, span
from htmler.tags import SafeString
from django.http import HttpResponse, HttpResponseNotFound
from .models import Project, TimeEntry
from django.core.urlresolvers import reverse
from decimal import Decimal


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
    try:
        year = int(year)
        week_no = int(week_no)
    except TypeError:
        return HttpResponseNotFound()
    contents = []
    html = bootstrap3(container(
        h1('Weekly report for week #%d (%d)' % (week_no, year)),
        *contents)
    )
    return HttpResponse(html)


def monthly(request, year, month_no):
    try:
        year = int(year)
        month_no = int(month_no)
    except TypeError:
        return HttpResponseNotFound()
    if not month_no in range(1, 12 + 1):
        return HttpResponseNotFound()
    data = [
        ('Project name 1', [
            (45, [
                ('some activity', Decimal('1.0')),
                ('some activity', Decimal('2.0')),
            ]),
            (46, [
                ('some activity', Decimal('1.5')),
            ]),
        ]),
        ('Project name 2', [
            (45, [
                ('some activity', Decimal('1.0')),
            ]),
        ]),
    ]
    with_tuple = lambda f: lambda x: f(*x)
    h_week = lambda week_no, activities: div(*(map(with_tuple(h_activity), activities) + [h_subtotal(week_no, activities)]), style='margin-bottom: 20px;')
    h_activity = lambda name, hours: div(name, ' ', span(str(hours) + 'h'))
    h_subtotal = lambda week_no, activities: strong('SubTotal for week #%d: %sh' % (week_no,sum(map(operator.itemgetter(1), activities))), style='font-style: italic; ')
    h_total = lambda weeks: strong('Total: ', sum(map(sum, map(functools.partial(map, operator.itemgetter(1)), map(operator.itemgetter(1), weeks)))))
    h_project = lambda name, weeks: div(h3(name), *(list(map(with_tuple(h_week), weeks)) + [h_total(weeks)]))
    contents = [h_project(
        ('%d. ' % (i + 1,)) + name,
        weeks
    ) for i, (name, weeks) in enumerate(data)]
    html = bootstrap3(container(
        h1('Monthly report for %s' % (datetime.datetime.strptime('%d-%d-1' % (year,month_no), '%Y-%m-%d').strftime('%B %Y'),)),
        *contents)
    )
    return HttpResponse(html)
