from django.shortcuts import render
from django.http import HttpResponse
from .models import LanguageInfo
from .forms import LanguageForm
# from django.views.generic import View,TemplateView
# Create your views here.

def Create(request):
    
    if request.POST:
        frm = LanguageForm(request.POST)
        if frm.is_valid:
            frm.save()
            frm = LanguageForm()
            
    else:
        frm = LanguageForm()

    return render(request,'create.html',{'frm':frm})

def List(request):
    language_set = LanguageInfo.objects.all().order_by('id')
    return render(request,'list.html',{'langs':language_set})

def Edit(request,pk):
    instance_to_be_edited = LanguageInfo.objects.get(pk=pk)
    frm = LanguageForm(instance=instance_to_be_edited)
    if request.POST:
        language = request.POST.get('language')
        designed_by = request.POST.get('designed_by')
        developer = request.POST.get('developer')
        os = request.POST.get('os')
        year = request.POST.get('year')
        description = request.POST.get('description')
        instance_to_be_edited.language = language
        instance_to_be_edited.designed_by = designed_by
        instance_to_be_edited.developer = developer
        instance_to_be_edited.os = os
        instance_to_be_edited.year = year
        instance_to_be_edited.description = description
        instance_to_be_edited.save()
        
        frm = LanguageForm()

    return render(request,'create.html',{'frm':frm})

def Delete(request,pk):
    instance = LanguageInfo.objects.get(pk=pk)
    instance.delete()
    language_set = LanguageInfo.objects.all()
    return render(request,'list.html',{'langs':language_set})

# class CBView(View):
#     def get(self,request):
#         return HttpResponse("CLASS BASE VIEWS ARE COOL !")
    
# class IndexView(TemplateView):
#     template_name = 'create.html'

    