from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('registration.htm')
  return HttpResponse(template.render())