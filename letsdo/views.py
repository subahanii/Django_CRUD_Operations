from django.shortcuts import render , redirect,HttpResponse
from os.path import join as isfile
from django.conf import settings
import os

#from letsdo.forms import EmployeeForm
from letsdo.models import Employee


# Create your views here.
def index(request):
    employees = Employee.objects.all()





#/home/rizwan/Desktop/fake/GulluDjango/first/media/app/img/gullu.jpg

    return render(request,"index.html", {'employees':employees})

def login(request,id=0,msg=''):
    print('id', id)
    if msg!='':
        return render(request, "login.html",{'msg':msg})

    if id==1:
        em=request.POST.get('email','')
        ep=request.POST.get('epass','')
        if em!='':
            try:
                employee = Employee.objects.get(email=em)

                if employee.email==em and employee.epass==ep:
                    request.session['username'] = em
                    print("login")
                    return redirect("/show")
                else:
                    print("else login")
                    return redirect("/login")
            except:
                print("exception")
                return redirect("/login")
        else:
            print("else em!=")
            return render(request,"login.html")

    return render(request,"login.html")




def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return redirect("/")


def register(request,id=0):
    if id==1:
        print(id)
        if request.method == 'POST':
            eid = request.POST.get('eid', '')
            ename = request.POST.get('ename', '')
            email = request.POST.get('email', '')
            epass = request.POST.get('epass', '')
            econtact = request.POST.get('econtact', '')
            eimg = request.FILES.get('myfile')
            emp = Employee(eid=eid, ename=ename, econtact=econtact, email=email, epass=epass, eimg=eimg)
            emp.save()
            return redirect("/login")

    return render(request,"register.html")


def show(request,uname=''):
    employees=Employee.objects.all()
    print(employees)

    if request.session.has_key('username'):
        uname = request.session['username']
        return render(request,"show.html",{'employees':employees,'uname':uname})
    else:
        return redirect("/")


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,"edit.html",{'employee' : employee } )


def update(request, id):
    employee = Employee.objects.get(id=id)
    eidd=employee.id

    employee.eid = request.POST.get('eid', '')
    employee.ename= request.POST.get('ename', '')
    employee.email = request.POST.get('email', '')
    employee.econtact = request.POST.get('econtact', '')
    employee.eimg = request.FILES.get('mfile')
    employee.eimg.name=str(eidd)+'.jpg'

    image_path = settings.MEDIA_ROOT + '/app/img/'+str(eidd)+'.jpg'


    if os.path.isfile(image_path):
        os.remove(image_path)

    employee.save()
    return redirect("/show")







def delete(request, id):

    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")




