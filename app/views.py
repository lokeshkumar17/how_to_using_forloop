from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'name':'loki'}
    return render(request,'forloop.html',context=d)
