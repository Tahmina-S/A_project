from django.shortcuts import render,HttpResponse,redirect
from .models import Purchase_Model
# Create your views here.
def home(request):
    return render(request,'index.html')
def table(request):
    obj=Purchase_Model.objects.all()
    return render(request,'table.html',{"o":obj})
def delete(request,a):
    obj=Purchase_Model.objects.get(id=a)
    obj.delete()
    return redirect('r')
def form(request):
    if request.method=='POST':
        nm=request.POST.get('n')
        add=request.POST.get('ad')
        ph=request.POST.get('p')
        em=request.POST.get('e')
        im=request.POST.get('i')
        obj=Purchase_Model(name=nm,address=add,phone=ph,email=em,photo=im)
        obj.save()
    return render(request,'form.html')
def update(request,b):
    obj=Purchase_Model.objects.get(id=b)
    if request.method=='POST':
        nm=request.POST.get('n')
        add=request.POST.get('ad')
        ph=request.POST.get('p')
        em=request.POST.get('e')
        im=request.POST.get('i')
        obj=Purchase_Model.objects.get(id=b)
        obj.name=nm
        obj.address=add
        obj.phone=ph
        obj.email=em
        obj.photo=im
        obj.save()
        return redirect('r')
    return render(request,'update.html', {'obj':obj})
 