from django.shortcuts import render
from .models import Book

# Create your views here.
from django.http import HttpResponse

def index(request): return HttpResponse("Welcome to my book shelf")