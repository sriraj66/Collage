from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password',widget=forms.PasswordInput)

    
    def action(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get("password")

        return {
            'username':str(username).upper(),
            'password':str(password).upper()
        }
    
        

class RegisterForm(forms.Form):
    username = forms.CharField(label='username',max_length=8)
    password = forms.CharField(label='password',widget=forms.PasswordInput,max_length=8)
    confirm = forms.CharField(label='Confirm Password',widget=forms.PasswordInput,max_length=8)

    def clean(self):
        user = self.cleaned_data.get('username')
        p1 = self.cleaned_data.get("password")
        p2 = self.cleaned_data.get('confirm')
        
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Password's Doesn't Match")
        
        return {
            'username':str(user).upper(),'password':str(p1).upper()
        }