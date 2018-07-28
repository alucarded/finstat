import logging

from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.generic import TemplateView
import generate_chart as gc
#from django.shortcuts import render

#from . import plots

logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = "index.html"


class PlotView(TemplateView):
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PlotView, self).get_context_data(**kwargs)
        context['plot'] = gc.generate_chart()
        return context
