# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class IndexView(TemplateView):
    """
    Index view for the portfolio page
    """
    #
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        return context
