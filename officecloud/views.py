# Create your views here.
from django.conf import settings
from django.shortcuts import render
from django.utils.module_loading import import_module

def index(request):
    apps = [import_module(appname) for appname in settings.INSTALLED_APPS]
    office_cloud_apps = []
    widgets = []
    office_cloud_apps = filter(lambda app: hasattr(app, 'IS_OFFICE_CLOUD'), apps)
    for app in office_cloud_apps:
        try:
            widget = {}
            widget['link'] = app.get_link
            widget['html'] = app.get_welcome_widget
            widgets.append(widget)
        except:
            pass
    return render(request, 'index.html', {'widgets': widgets})