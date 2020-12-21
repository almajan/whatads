from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
@csrf_exempt
def send_messages(request):
    print('hi')
    return JsonResponse({
        'Status':'Ok',
    },encoder=JSONEncoder)


def send_images(request):
    print('hi')
    return JsonResponse({
        'Status':'Ok',
    },encoder=JSONEncoder)



def send_videos(request):
    print('hi')
    return JsonResponse({
        'Status':'Ok',
    },encoder=JSONEncoder)



def send_voices(request):
    print('hi')
    return JsonResponse({
        'Status':'Ok',
    },encoder=JSONEncoder)



def check_delivery(request):
    print('hi')
    return JsonResponse({
        'Status':'Ok',
    },encoder=JSONEncoder)



def check_seen(request):
    print('hi')
    return JsonResponse({
        'Status':'Ok',
    },encoder=JSONEncoder)
