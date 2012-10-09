from django.shortcuts import render_to_response
from monitoring.models import Sensor

def index(request):
    sensor_list = Sensor.objects.all().order_by('-id_number')[:4]
    return render_to_response('monitoring/index.html',{'sensor_list': sensor_list})
