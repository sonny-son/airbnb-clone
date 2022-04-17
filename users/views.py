from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms


class LoginView(FormView):
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    # 해당 form이 맞는지 확인하는 함수, 성공하면 success_url로 자동 연결
    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))
