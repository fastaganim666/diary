from django import forms


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

