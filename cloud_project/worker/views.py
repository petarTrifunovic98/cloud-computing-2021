from django.shortcuts import render
from .serializers import WorkerSerializer
from .models import Worker
from django.http import JsonResponse


def workers_json(request):
    workers = Worker.objects.all()
    serializer = WorkerSerializer(workers, many=True)
    return JsonResponse(serializer.data, safe=False, status=200)

