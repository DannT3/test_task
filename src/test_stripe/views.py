from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World!")

def show_item_info(request):
    pass




