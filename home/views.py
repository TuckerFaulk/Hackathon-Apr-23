from django.views.generic import TemplateView
from django.shortcuts import render


class Index(TemplateView):
    template_name = 'home/index.html'


class AboutUs(TemplateView):
    template_name = 'home/about-us.html'


class Resources(TemplateView):
    template_name = 'home/resources.html'


def handler404(request, exception):
    """ Custom 404 page """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """ Custom 500 page """
    return render(request, "errors/500.html", status=500)
