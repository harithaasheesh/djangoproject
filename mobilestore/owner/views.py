from django.shortcuts import render,redirect
from owner import forms

# Create your views here.
def add_mobile(request):
    if request.method=="GET":
        form=forms.MobileaddForm()
        context={}
        context["form"]=form
        return render(request,"mobile_add.html",context)
    if request.method=="POST":
        form=forms.MobileaddForm(request.POST)
        if form.is_valid():
            mobile_name=form.cleaned_data["mobile_name"]
            mobile_model=form.cleaned_data["mobile_model"]
            company=form.cleaned_data["company"]
            price=form.cleaned_data["price"]
            print(mobile_name,mobile_model,company,price)
            return redirect("addmobile")
        else:
            return render(request,"mobile_add.html",{'form':form})