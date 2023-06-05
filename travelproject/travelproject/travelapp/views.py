from django.shortcuts import render

# Create your views here.

from.models import Place,Bloggers
# from.models import peoples
def index(request):
    obj=Place.objects.all()
    res=Bloggers.objects.all()
    return render(request,"index.html",{'result':obj,'result1':res})
