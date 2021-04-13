from django.shortcuts import render,HttpResponse,redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def  shit_list(request):
    shits = models.Shit.objects.all().order_by('-date')
    args = {'shits':shits}
    return render(request, 'shit/shitlist.html',args)


def shit_detail(request,slug):
    # return HttpResponse(slug)
    shit = models.Shit.objects.get(slug=slug)
    return render(request, 'shit/shit_detail.html',{'shit':shit})

@login_required(login_url="/accounts/login")
def create_shit(request):
    if request.method == 'POST':
        form = forms.CreateShit(request.POST,request.FILES)
        if form.is_valid:
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('shits:list')
    else:
        form = forms.CreateShit()
    return render(request, 'shit/shits/create_shit.html',{'form':form})
