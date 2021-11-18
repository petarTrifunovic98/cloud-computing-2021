from django.shortcuts import render
from .serializers import ZaposleniSerializer
from .models import Zaposleni
from django.http import JsonResponse


def zaposlenis_json(request):
    zaposlenis = Zaposleni.objects.all()
    serializer = ZaposleniSerializer(zaposlenis, many=True)
    return JsonResponse(serializer.data, safe=False, status=200)

def zaposleni_json(request, id):
    zaposleni = Zaposleni.objects.get(id=id)
    serializer = ZaposleniSerializer(zaposleni)
    return JsonResponse(serializer.data, safe=False, status=200)
