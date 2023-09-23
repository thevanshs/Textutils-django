# I have created this file - vansh

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyzetext(request):
    textvalue=request.POST.get('text','default')
    remove=request.POST.get('Remove','off')
    upper=request.POST.get('Upper','off')
    lower=request.POST.get('Lower','off')
    spaces=request.POST.get('Extra','off')
    if(remove=='on'):
        ans=""
        punctuations='''.?""',-—!:;()[]…/'''
        for char in textvalue:
            if char not in punctuations:
                ans=ans+char
        if(len(ans)!=0):
            count=ans.split(" ")
            cvalue=len(count)
            ctime=cvalue*0.008
        else:
            cvalue=0
            ctime=cvalue*0.008
        params={'purpose':'Removed punctuations','result':ans,'words':cvalue,'time':ctime}
        return render(request,'analyze.html',params)
    elif(upper=='on'):
        ans=textvalue.upper()
        if(len(ans)!=0):
            count=ans.split(" ")
            cvalue=len(count)
            ctime=cvalue*0.008
        else:
            cvalue=0
            ctime=cvalue*0.008
        params={'purpose':'Upper Case','result':ans,'words':cvalue,'time':ctime}
        return render(request,'analyze.html',params)
    elif(lower=='on'):
        ans=textvalue.lower()
        if(len(ans)!=0):
            count=ans.split(" ")
            cvalue=len(count)
            ctime=cvalue*0.008
        else:
            cvalue=0
            ctime=cvalue*0.008
        params={'purpose':'Lower Case','result':ans,'words':cvalue,'time':ctime}
        return render(request,'analyze.html',params)
    elif(spaces=='on'):
        ans= ' '.join(textvalue.split())
        if(len(ans)!=0):
            count=ans.split(" ")
            cvalue=len(count)
            ctime=cvalue*0.008
        else:
            cvalue=0
            ctime=cvalue*0.008
        params={'purpose':'Remove Extra Spaces','result':ans,'words':cvalue,'time':ctime}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error Tip:- select at least one checkbox")

