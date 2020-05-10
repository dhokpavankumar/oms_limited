from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignupForm
from testapp.models import student
from django.http import HttpResponseRedirect




def Home_page_view(request):
    return render(request, 'testapp/index.html')

def logout_view(request):
    return render(request, 'testapp/logout.html')

@login_required
def add_student_view(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
        return Home_page_view(request)
    return render(request,'testapp/addstudent.html', {'form':form})

@login_required
def list_student_view(request):
    list_student=student.objects.all()
    return render(request,'testapp/liststudent.html',{'list_student':list_student})

def signup_view(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        # if form.is_valid():
        #     print('Basic information provided by student')
        #     print('Name', form.cleaned_data['name'])
        #     print('Password: ', form.cleaned_data['password'])
        #     print('Email: ', form.cleaned_data['email'])

        user=form.save()
        user.set_password(user.password)
        user.save()
        return  HttpResponseRedirect('accounts/login')
    return render(request, 'testapp/signup.html', {'form': form})



