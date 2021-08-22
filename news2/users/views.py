from django.shortcuts import redirect, render, reverse
from django.views import View
from.forms import LoginForm
from django.contrib.auth import login, authenticate

class LoginView(View):
    def get(self, request):
        # TODO: set up redirect url if authenticated
        if request.user.is_authenticated:
            return redirect(reverse('post_list_url'))
        form = LoginForm()
        return render(request, 'login.html', context={'form': form})

    def post(self, request):
        bound_form = LoginForm(request.POST)

        if bound_form.is_valid():
            username = bound_form.cleaned_data.get('username')
            password = bound_form.cleaned_data.get('password')
            user =  authenticate(username=username, password=password) #User
            if user:
                login(request, user)
                #TODO: URGENT add redirect url after login
                return redirect(reverse('post_list_url'))
        return render(request, 'login.html', context={'form': bound_form})
