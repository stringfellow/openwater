#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView

from .views import (
    MapView, AddView, ParamRowView, TestRowView, MeasurementView,
    DownloadView, ReportView, MeasurementPopupView
)
from .models import Test


urlpatterns = patterns(
    '',
    url(r'^map/', MapView.as_view(), name='observations-map'),
    url(r'^report/', ReportView.as_view(), name='observations-report'),
    url(r'^download/', DownloadView.as_view(), name='observations-download'),
    url(r'^detail/(?P<pk>\d+)/$', MeasurementView.as_view(), name='observations-detail'),
    url(r'^detail/(?P<pk>\d+)/popup/$', MeasurementPopupView.as_view(), name='observations-detail-popup'),
    url(r'^add/$', AddView.as_view(), name='observations-add'),
    url(r'^add/param/$', ParamRowView.as_view(), name='observations-add-param'),
    url(r'^add/test/$', TestRowView.as_view(), name='observations-add-test'),

    url(r'^tests/$',
        ListView.as_view(
            template_name='test_list.html',
            queryset=Test.objects.order_by('parameter__name')
        ), name='observations-tests'),
    url(r'^tests/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Test,
            template_name='test_detail.html'
        ), name='observations-test-detail'),
)
