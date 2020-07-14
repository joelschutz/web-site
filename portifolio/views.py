from django.shortcuts import render
from django.http import HttpResponse


home = lambda request : render(request, 'pages/index.html')

