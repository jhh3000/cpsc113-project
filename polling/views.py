import random

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

DEFAULT_PASSWORD = 'DEFAULT_PASSWORD'

# Create your views here.

def dashboard(request):
	template = "dashboard.html"
	context = {}
	return render(request, template, context)

def dashboard_data(request):
	num1 = random.random() * 25 + 25
	num2 = random.random() * 25 + 25
	response = JsonResponse({ 'data': [num1, num2]})
	return response

def poll(request):
	template = "poll.html"
	context = {}
	return render(request, template, context)

def portal(request):
	template = "portal.html"
	context = {}
	return render(request, template, context)

def studentlogin(request):
	# make sure code is correct
	code = request.POST.get('code')
	email = request.POST.get('email')
	if code != "a123" or not email:
		return redirect('home')

	# create user if doesn't exist
	if not User.objects.filter(email=email).exists():
		User.objects.create_user(email, email, DEFAULT_PASSWORD)

	# log the user in
	user = authenticate(username=email, password=DEFAULT_PASSWORD)
	login(request, user)

	return redirect('poll')

def teacherlogin(request):
	# make sure code is correct
	code = request.POST.get('code')
	if code == "teacher":
		return redirect('dashboard')
	else:
		return redirect('home')
