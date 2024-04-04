from django.shortcuts import render
from .models import Event
from .serializer import EventSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import csv
from .forms import UploadFileForm, DateForm
import datetime 
from django.shortcuts import render

from datetime import datetime, timedelta
from .models import Event

def search_events(request):
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            search_date = form.cleaned_data['search_date']
            end_date = search_date + timedelta(days=14)
            events = Event.objects.filter(date__range=[search_date, end_date])
            return render(request, 'search_results.html', {'events': events})
    else:
        form = DateForm()
    return render(request, 'search.html', {'form': form})


def upload_file(request):
    uploaded_data = None
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            if csv_file.name.endswith('.csv'):
                with csv_file.open(mode='r') as f:
                    data = csv.reader((line.decode('utf-8') for line in f), delimiter=',')
                    uploaded_data = []
                    for row in data:
                        if len(row) == 6:
                            event_name, city_name, date_str, time, latitude, longitude = row
                            try:
                               
                                date_obj = datetime.datetime.strptime(date_str, '%d-%m-%Y').date()
                                event = Event(event_name=event_name, city_name=city_name, date=date_obj, time=time, latitude=latitude, longitude=longitude)
                                uploaded_data.append(event)
                            except ValueError:
                                print(f"Invalid date format: {date_str}")
                    Event.objects.bulk_create(uploaded_data)
                    return render(request, 'success.html', {'uploaded_data': uploaded_data})
            else:
                return render(request, 'error.html', {'error': 'Please upload a CSV file.'})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


@api_view(['Get'])

def Event_details(request):
    Events = Event.objects.all()
    serializer = EventSerializer(Events, many=True)


    return Response(serializer.data)




@api_view(['POST'])

def create_event(request):
    serializer = EventSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_event(request, id):
    
    Events = Event.objects.get(id=id)


    serializer = EventSerializer(instance=Events, data=request.data)

    if serializer.is_valid():

        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])

def delete_event(request, id):
    Events = Event.objects.get(id=id)
    Events.save()

    return Response("event got deleted")


@api_view(['Get'])

def view_events(request,id):
    Events = Event.objects.get(id=id)
    serializer = EventSerializer(Events)


    return Response(serializer.data)
