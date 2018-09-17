from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, LoginForm

# Create your views here




class LoginFormView(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard:index')

        return render(request, self.template_name, {'form': form})


class UserFormView(View):
    form_class = UserForm
    template_name = 'accounts/signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username = username, password= password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard:index')

        return render(request, self.template_name, {'form': form})






















