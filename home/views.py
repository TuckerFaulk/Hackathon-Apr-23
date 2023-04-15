from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'home/index.html'


class AboutUs(TemplateView):
    template_name = 'home/about-us.html'


class Resources(TemplateView):
    template_name = 'home/resources.html'
