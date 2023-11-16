from django.shortcuts import render

# Create your views here.
def login(request):
    d1={'username':'Siva Sai Kumar Kongala','age':'23'}
    
    return render(request,'login.html',context=d1)

def data_render(request):
    data='This data is Assumption'
    d={'assumption':data}
    return render(request,'data_render.html',context=d)