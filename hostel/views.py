from __future__ import unicode_literals

from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from models import User,Room,Complain
from django.contrib.auth import authenticate, login as lgn, logout as lgt
from .forms import *
from django.db.models import Q
from django.contrib import messages

def home(request):
	usr=request.user.is_authenticated()
	if usr:
		if request.method=="GET":
			return render(request,'hostel/home.html')
	else:
		return HttpResponse('user not logged in')


def all_students(request):
	usr=request.user.is_authenticated()
	if usr:
		if request.method=="GET":
			box=User.objects.filter(is_superuser=False).order_by('rank')	
			context={'member': box }
			return render(request,'hostel/all_students.html', context)
		else:
			return HttpResponse('no')
	else:
		return HttpResponse('User not logged in')
def student(request):
	usr=request.user.is_authenticated()	
	if usr:
		if request.method=="GET":
			return render(request,'hostel/student.html')
	else:
		return HttpResponse('not logged in')
		
def register(request):
	if request.method=="GET":
		return render(request,'hostel/sign_up.html')
	else:
		box=User(username=request.POST['user'], first_name=request.POST['first'],
		 last_name=request.POST['last'],
		 email=request.POST['email'],phone=request.POST['phone'], 
		 fee_slip=request.POST['fee-slip'],
		 rank=request.POST['rank'],gender=request.POST['gender'],
		  clas=request.POST['clas'], img=request.FILES['imgs'])
		box.set_password(request.POST['password'])	
		box.save()
		return HttpResponseRedirect(reverse('login'))

def login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		
		user=authenticate(username=username, password=password)
		if user:
			lgn(request,user)
			if request.user.is_superuser:
				return HttpResponseRedirect(reverse('home'))
			else:
				return HttpResponseRedirect(reverse('student'))
		else:
			context={'error':'invalid user'}
			return render(request,'hostel/login.html', context)
	else:
		return render(request,'hostel/login.html')
		
def logout(request):
	if request.method=="GET":
		lgt(request)
		return HttpResponseRedirect(reverse('login'))

def contact(request):
	usr=request.user.is_authenticated()	
	if usr:
		if request.method=="GET":
			return render(request,'hostel/contact.html') 
	else:
		return HttpResponse('not logged in')

def gallery(request):
	usr=request.user.is_authenticated()	
	if usr:
		if request.method=="GET":
			return render(request,'hostel/gallery.html')
	else:
		return HttpResponse('not logged in')


def room(request):
	usr=request.user.is_authenticated()	
	if usr:
		if request.method=="POST":
			form = room_form(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('home'))
		
		else:
			form = room_form()
			return render(request,'hostel/room.html',{'frm':form})
	else:
		return HttpResponse('user not login')

def status(request):
	ur=request.user.is_authenticated()

	if ur:
		if request.method=="GET":		
			box=Room.objects.filter(usr=request.user)
			context={'data': box }
			return render(request,'hostel/status.html',context)
		else:
			return HttpResponse('user not found')
	else:
		return HttpResponse('not logged in') 	

def complain(request):
	usr=request.user.is_authenticated()
	if usr:
		if request.method=="GET":
			return render(request,'hostel/complainstu.html')
		else:
			if request.method=="POST":
				box=Complain(usr=request.user, room_no=request.POST['rno'], 
					Complain=request.POST['complain'],
					date=request.POST['date'])
				box.save()
				return render(request,'hostel/student.html')
			else:
				return HttpResponse('Data is invalid')
	else:
		return HttpResponse('user not login')

def adcomplain(request):
	usr=request.user.is_authenticated()
	if usr:
		if request.method=="GET":
			box=Complain.objects.all()
			context={'data':box} 
			return render(request,'hostel/complain.html',context)
		else:
			return HttpResponse('no any complain')
	else:
		return HttpResponse('not logged in')

def alloted(request):
	ur=request.user.is_authenticated()

	if ur:
		if request.method=="GET":		
			box=Room.objects.all()
			context={'data': box }
			return render(request,'hostel/alloted.html',context)
		else:
			return HttpResponse('page not found')
	else:
		return HttpResponse('not logged in')


def search(request):
	if request.method=="POST":
		match=User.objects.filter(Q(username__icontains=request.POST['search']) 
			| Q(fee_slip__icontains=request.POST['search']))			
		if match:
			return render(request,'hostel/search.html', {'key':match})
		else:
			 return HttpResponse('result not found')
	else:
		return render(request,'hostel/search.html')

def seats(request):
	usr=request.user.is_authenticated()
	if usr:
		if request.method=="GET":
			return render(request,'hostel/seats.html')
	else:
		return HttpResponse('user not logged in')


def vacate(request):
	usr=request.user.is_authenticated()
	if usr:
		if request.method=="GET":
			return render(request, 'hostel/vacate.html')
		else:
			seat=Room.objects.filter(room_no=request.POST['r_no'])
			context={'result':seat}
			return render(request,'hostel/vacate.html',context)
	else:
		return HttpResponse('user not logged in')

def edit(request):
	usr=request.user.is_authenticated()
	if usr:
		if request.method=="GET":
			box=Room.objects.get()
			context={'data': box}
			return render(request, 'hostel/edit.html', context)
	else:
		return HttpResponse('user not logged in')

	# Create your views here.

#code for Room Allot
'''	if request.method=="GET":
			return render(request,'hostel/room.html')
		else:
			box=Room(hname=request.POST['hname'], room_no=request.POST['room_no'], 
				block=request.POST['block'], floor=request.POST['floor'], bed_no=request.POST['bed_no'])
			box.save()
			return HttpResponseRedirect(reverse('home')) '''

#code for Complain Box
'''	form = complain_form(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('home'))
			else:
				return HttpResponse('form is not valid')
		else:
			form = complain_form()
			return render(request, 'hostel/complainstu.html', {'frm':form}) '''
