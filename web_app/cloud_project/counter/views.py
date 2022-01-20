from django.shortcuts import render
from .serializers import CounterSerializer
from .models import Counter
from django.http import JsonResponse

def increase_counter(request):
    all_counters = Counter.objects.all()
    if len(all_counters) == 0:
        c = Counter()
    else:
        all_counters = all_counters.order_by('id')
        c = all_counters[0]
    c.counter += 1
    c.save()
    serializer = CounterSerializer(c, many=False)
    return JsonResponse(serializer.data, safe=False, status=200)
