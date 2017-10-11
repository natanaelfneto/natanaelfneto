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
    template_name = "index2.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        return context

# Create your views here.
def Index2View(request):
    """
    Index view for the portfolio page
    """
    return render(request, 'detail.html')
