from django import forms

class MobileaddForm(forms.Form):
    mobile_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile_model=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    company=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))


    def clean(self):
        cleaned_data=super().clean()
        price=cleaned_data["price"]
        if price<0:
            msg="invalid price"
            self.add_error("price",msg)