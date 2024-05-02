

from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth


# Create your views here.
def index(request):
    return render(request,"index.html") 

def allLogin(request):
    return render(request,"allLogin.html") 

def donorSignup(request):
  
    if request.method == "POST":
        name1=request.POST.get("name")
        contact1=request.POST.get("contact")
        email1=request.POST.get('email')
        password1=request.POST.get("pass1")
        password2=request.POST.get("pass2")
        donorpic1=request.FILES.get("donorpic")
        address1=request.POST.get("address")
        
        # if password1==password2:
        #     if User.objects.filter(username)

        try:
            user=User.objects.create_user(username=email1, password=password1,)
            user.save()
            donor=Donor.objects.create( name=name1,contact=contact1,email=email1,password=password1,donorpic=donorpic1,address=address1)
            donor.save()
            error="no"
        except:
             error="yes"    
    return render(request,"donorSignup.html",locals())

def donorLogin(request):
        if request.method == "POST":
            username1=request.POST.get("username")
            password1=request.POST.get("password")
            donor = auth.authenticate(request,username=username1,password=password1)
           
            if donor is not None:
                auth.login(request,donor)
                # return redirect('donorHome')
                error="no"
            else:
                # return redirect('donorLogin')
                error="yes"
        return render(request,"donorLogin.html",locals())    



def donorReset(request):
    return render(request,"donorReset.html")
    
def donorHome(request):
    donor = Donor.objects.all()
    data={
        "donors":donor,
    }

    if not request.user.is_authenticated:
        return redirect("donor_login")
    return render(request,"donorHome.html",data)

def donateNow(request):

        if request.method == "POST":
            donorname1=request.POST.get("donorname")
            donationname1=request.POST.get("donationname")
            donationpic1=request.FILES.get("donationpic")
            collectionloc1=request.POST.get('collectionloc')
            description1=request.POST.get("description")
           
            try:
                Donation.objects.create(donorname=donorname1,donationname=donationname1,donationpic=donationpic1,description=description1,status="pending")
                error= "no"
            except:
                error= "yes" 
        return render(request,"donateNow.html",locals())

def donationHistory(request):

    return render(request,'donationHistory.html',locals())


def logout_donor(request):
    logout(request)
    return redirect ("index.")



def footer(request):
    return render(request,"footer.html")

def adminLogin(request):
        if request.method == "POST":
            username1=request.POST.get("username")
            password1=request.POST.get("password")
            User = authenticate(username=username1,password=password1)
      
            if User.is_staff:
                login(request,User)
                error="no"
            else:
                 error="yes"
        return render(request,"adminLogin.html",locals())


def adminHome(request):
    if not request.user.is_authenticated:
      return redirect("admin_login")
    return render(request,"adminHome.html")

def volunteerLogin(request):
        if request.method == "POST":
            username3=request.POST.get("username")
            password3=request.POST.get("password")
            volunteer = auth.authenticate(request,username=username3,password=password3)
           
            if volunteer is not None:
                auth.login(request,volunteer)
                # return redirect('volunteerHome')
                error="no"
            else:
                error="yes"
                # return redirect('volunteerLogin')

        return render(request,"volunteerLogin.html",locals())

def volunteerSignup(request):

        if request.method == "POST":
            name1=request.POST.get("name")
            contact1=request.POST.get("contact")
            email1=request.POST.get('email')
            password1=request.POST.get("pass1")
            volunteerpic1=request.FILES.get("volunteerpic")
            idpic1=request.FILES.get("idpic")
            address1=request.POST.get("address")
           
        try:
            user=User.objects.create_user(username=email1, password=password1,)
            user.save()
            volunteer=Volunteer.objects.create( name=name1,contact=contact1,email=email1,password=password1,volunteerpic=volunteerpic1,idpic=idpic1,address=address1,)
            volunteer.save()
            error="no"
        except:
             error="yes"  
        return render(request,"volunteerSignup.html",locals())

def volunteerHome(request):
    return render(request,"volunteerHome.html",locals())