from django.shortcuts import render
from accounts.session_true import session
# Create your views here.

def index(request):
    return render(request, 'about_us/index.html')
