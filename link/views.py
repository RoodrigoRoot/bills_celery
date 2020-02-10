from django.shortcuts import render
from ftplib import FTP
from django.views import View
from .tasks import *
# Create your views here.

class IndexView(View):
    
    def get(self, request, *args, **kwargs):
        
        return render(request, "index.html", locals())
    
    def post(self, request, *args, **kwargs):
        get_bills_moth.delay()
        return render(request, "index.html", locals())
    
