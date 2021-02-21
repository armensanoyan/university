from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Universities

@login_required(login_url='login/')
def index(request):
	if request.POST:
		name = request.POST['name']
		address = request.POST['address']
		subjects = request.POST['subjects']
		
		if Universities.objects.filter(name=name).exists():
			universities = Universities.objects.all()
			content = {
			'error':'this university already exists',
			'universities':universities,
		}
			return render(request, 'univerApp/main.html',content)
		
		elif name is None or name == '':
			universities = Universities.objects.all()	
			content = {
				'universities':universities,
				'error':"please provide university name",
			}
			return render(request, 'univerApp/main.html', content)
		elif address is None or address == '':
			universities = Universities.objects.all()	
			content = {
				'universities':universities,
				'error':"please provide university address",
			}
			return render(request, 'univerApp/main.html', content)
		
		elif len(subjects.split(',')) < 2:
			universities = Universities.objects.all()	
			content = {
				'universities':universities,
				'error':"please provide more subjects",
			}
		else:
			Universities.objects.create(name=name, address=address, subjects=subjects)
			universities = Universities.objects.all()	
			content = {
				'universities':universities,
				'error':None,
			}

		return render(request, 'univerApp/main.html', content)
	else:
		universities = Universities.objects.all()
		content = {
			'universities':universities,
			'error':None
		}
		return render(request, 'univerApp/main.html', content)


@login_required(login_url='login/')
def university(request, university_name):
	try:
		university = Universities.objects.get(name=university_name)
		return render(request, 'univerApp/university.html', {'university':university})

		# render(request, 'universityApp/university.html', university)
	except:
		content = {
		'error':'something went wrong',
		'universities':Universities.objects.all(),
	}
		return redirect('index')



def login(request):
    return render(request, 'univerApp/login.html')

def authorization(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return redirect('index')
	else:
		return render(request, 'univerApp/login.html', {'error':'wrong username or password'})

def logout_view(request):
    logout(request)
    return redirect(request, 'univerApp/login.html')

def signin(request):
    return render(request, 'univerApp/signin.html')

def register(request):
    user_exists = User.objects.filter(username=request.POST['username']).count()
    email_exists = User.objects.filter(username=request.POST['email']).count()
    if user_exists + email_exists:
        return render(request,'univerApp/signin.html',{ 'error':'user with this username or email already exists!'})
    else:
        User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        return HttpResponseRedirect('/')

def	remove(request, university_name):
	Universities.objects.filter(name=university_name).delete()
	return redirect('index')