from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        print(email, email.endswith(".edu"))
        if email.endswith(".edu"):
            print(email)
            raise forms.ValidationError("This is invalid! don't enter .edu emails")
        return email