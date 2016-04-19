import random

from django.shortcuts import render, redirect
from django.http import JsonResponse

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
	template = "portal.html"
	context = {}
	return render(request, template, context)

def teacherlogin(request):
	code = request.POST.get('code')
	if code == "teacher":
		return redirect('dashboard')
	else:
		return redirect('home')
