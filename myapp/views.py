from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm, StudentForm
from django.contrib.auth.decorators import login_required
from .models import student
# Create your views here.


def Home(request):
    
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        student_form = StudentForm(request.POST, request.FILES)
        if user_form.is_valid() and student_form.is_valid():
            # Create the User object
            user = user_form.save()

            # Create the Student object
            Student = student_form.save(commit=False)
            Student.user = user
            Student.save()
            
            return redirect('/login')
    else:
        user_form = CreateUserForm()
        student_form = StudentForm()
    return render(request, 'index.html', {'user_form': user_form, 'student_form': student_form})

def loginpage(request):
    
    if request.method=="POST":
        username=request.POST.get('user_name')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/dashboard')
    return render(request,'login.html')
@login_required(login_url="/login")
def dashboard(request):
    student_obj = student.objects.get(user=request.user)
    return render(request,"dashboard.html",{'data':student_obj})
def logout1(request):
    logout(request)
    return redirect("/login")