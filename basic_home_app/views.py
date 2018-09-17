from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    return render(request, 'basic_home_app/index.html')