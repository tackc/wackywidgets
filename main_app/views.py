from django.shortcuts import render
from .models import Widget
from .forms import WidgetForm
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect

# Create your views here.

class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'

def index(request):
    # add conditional based on request.method
    form = WidgetForm(request.POST)
    # if post do this
    if form.is_valid():
        new_widget = form.save()
        return HttpResponseRedirect('/')
    # else, if get do this
    else:
        form = WidgetForm()
        widget_list = Widget.objects.all()
    return render(request, 'index.html', {'form': form, 'widget_list': widget_list})