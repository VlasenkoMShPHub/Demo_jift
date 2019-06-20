from django import forms


class PredictForm(forms.Form):
    item1 = forms.CharField(label='Item 1:', max_length=1000, required=False)
    item2 = forms.CharField(label='Item 2:', max_length=1000, required=False)
    item3 = forms.CharField(label='Item 3:', max_length=1000, required=False)
