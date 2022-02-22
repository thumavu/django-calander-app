from django.shortcuts import render
from django.http import HttpResponse
from .models import Holidays
from dotenv import load_dotenv
import os
import requests
import logging

logger = logging.getLogger(__name__)
load_dotenv()

def index(request):
    return render(request, 'index.html')
