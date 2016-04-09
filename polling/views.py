from django.shortcuts import render, redirect
from django.template import loader
from django.db.models import Q
from django.contrib.auth.hashers import check_password, make_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# from .models import User, Task

# Create your views here.
def portal(request):
    
    return render(request, 'portal.html', context)