# View functions for handling HTTP requests and returning HTTP responses
from django.shortcuts import render, redirect
from django.http import HttpResponse
def home(request):
    return HttpResponse("Welcome to the Home Page!")