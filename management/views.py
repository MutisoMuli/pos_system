from django.shortcuts import render
from django.http import HttpResponse

def management_home(request):
     return render(request, 'management/management.html')