from django.shortcuts import render
from forms_app import forms
from Django_Demo_App_1 import forms as forms2
# Create your views here.

def index(request):
    return render(request,'forms_app/forms.html')

def form_name(request):
    form=forms.Form()
    if request.method == 'POST':
        form=forms.Form(request.POST)
        if form.is_valid():
            print("VALID!")
            print('NAME: '+form.cleaned_data['name'])
            print('EMAIL: '+form.cleaned_data['email'])
            print('TEXT: '+form.cleaned_data['text'])

    return render(request,'forms_app/forms.html',{'form':form})
