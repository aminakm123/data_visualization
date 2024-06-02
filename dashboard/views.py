import json
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from .models import DataPoint
from .forms import DataPointForm

def index(request):
    return render(request, 'index.html')


def parse_and_store_json(request):
    with open('static/jsondata.json') as f:
        data = json.load(f)

    for item in data:
        DataPoint.objects.create(
            end_year=item['end_year'],
            intensity=item['intensity'],
            sector=item['sector'],
            topic=item['topic'],
            insight=item['insight'],
            url=item['url'],
            region=item['region'],
            start_year=item['start_year'],
            impact=item['impact'],
            added=item['added'],
            published=item['published'],
            country=item['country'],
            relevance=item['relevance'],
            pestle=item['pestle'],
            source=item['source'],
            title=item['title'],
            likelihood=item['likelihood']
        )
    context ={
        "success_message" : "Data parsed and stored successfully"
    }
    return render(request, 'parse_json.html', context=context)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def dashboard(request):
    datapoint = DataPoint.objects.all()
    if request.method == 'GET' and is_ajax(request):
        start_year = request.GET.get('start_year')
        intensity = request.GET.get('intensity')
        topic = request.GET.get('topic')
        relevance = request.GET.get('relevance')
        region = request.GET.get('region')

        filter_conditions = Q()
        if start_year is not None and start_year != "null":
            filter_conditions &= Q(start_year__gte=start_year)
        if intensity is not None and intensity != "null":
            filter_conditions &= Q(intensity__gte=intensity)
        if topic is not None and topic != "null":
            filter_conditions &= Q(topic=topic)
        if relevance is not None and relevance != "null":
            filter_conditions &= Q(relevance=relevance)
        if region is not None and region != "null":
            filter_conditions &= Q(region=region)


        filtered_data = DataPoint.objects.filter(filter_conditions).values()
        return JsonResponse(list(filtered_data), safe=False)
    
   
    form = DataPointForm(request.POST or None)
    
    context = {
        "datapoint": datapoint,
        "form": form
    }
    return render(request, 'dashboard.html', context=context)




