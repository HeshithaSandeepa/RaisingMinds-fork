from django.shortcuts import render
from users.models import User

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def home(request):

    user = request.user

    return render(request,'app/home.html',{'user':user})

def project(request):

    return render(request,'app/projects.html')