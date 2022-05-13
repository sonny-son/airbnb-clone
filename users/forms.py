from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "input mb-3"})
    )
    # passwordinput 비밀번호가 안보이게 가리게함
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "input mb-3"}
        )
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email")
        widgets = {
            "first_name": forms.TextInput(
                attrs={"placeholder": "First Name", "class": "input"}
            ),
            "last_name": forms.TextInput(
                attrs={"placeholder": "Last Name", "class": "input"}
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "Email Name", "class": "input"}
            ),
        }

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "input"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm Password", "class": "input"}
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError(
                "That email is already taken", code="existing_user"
            )
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password)
        user.save()


class UpdateProfileForm(forms.ModelForm):
    # view에서 보내는 pk 받기
    def __init__(self, pk, *args, **kwargs):
        # we explicit define the foo keyword argument, cause otherwise kwargs will
        # contain it and passes it on to the super class, who fails cause it's not
        # aware of a foo keyword argument.
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        self.pk = pk

    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email")
        widgets = {
            "first_name": forms.TextInput(
                attrs={"placeholder": "First Name", "class": "input"}
            ),
            "last_name": forms.TextInput(
                attrs={"placeholder": "Last Name", "class": "input"}
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "Email Name", "class": "input"}
            ),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError(
                "That email is already taken", code="existing_user"
            )
        except models.User.DoesNotExist:
            return email

    def save(self):
        user = models.User.objects.get(pk=self.pk)
        email = self.cleaned_data.get("email")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        user.username = email
        if first_name:
            user.first_name = first_name
            print(first_name)
        if last_name:
            user.last_name = last_name
        user.save()
