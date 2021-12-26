from .models import Employee
from django.shortcuts import render,redirect
from .forms import CreateEmployee
from django.contrib.auth import login, logout,  authenticate
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        takingValue = CreateEmployee(request.POST)
        if takingValue.is_valid():
            upass = takingValue.save(commit=False)
            upass.set_password(takingValue.cleaned_data['password'])
            takingValue.save()
            user = takingValue.cleaned_data.get('name')
            messages.success(request, 'The account for '  + user + ' created succesfully!')
        return redirect ('login')
    else:
        takingValue = CreateEmployee()
    dis = Employee.objects.all()
    return render (request, 'employee/register.html', {'form':takingValue, 'dis': dis})


def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password = password)

        if user is not None:
            login(request, user)
            return redirect('success')
        else:
            messages.info(request,"Email or Password is incorrect!")

    context={}
    return render(request, 'employee/login.html' , context)


def logoutUser(request):
    logout(request)
    return redirect('login')




def deleteEmployee(request,id):
    if request.method == 'POST':
        deletingValue = Employee.objects.get(pk=id)
        deletingValue.delete()
        return redirect('register')

def updateEmployee(request,id):
    if request.method == 'POST':
        takingValue =Employee.objects.get(pk=id)
        storeValue = CreateEmployee(request.POST, instance=takingValue)
        if takingValue.is_valid():
            takingValue.save()
    else:
        takingValue =Employee.objects.get(pk=id)
        storeValue = CreateEmployee(instance=takingValue)
    return render(request, 'employee/update.html' ,{'form' : storeValue})


def success(request): 
     return render (request, 'employee/success.html')