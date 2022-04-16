from django import forms


class LoginForm(forms.Form):

    email = forms.EmailField()
    # passwordinput 비밀번호가 안보이게 가리게함
    password = forms.CharField(widget=forms.PasswordInput)
