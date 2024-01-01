from django.shortcuts import render,redirect
from . models import Vehicles,Category
from . forms import VehicleForm,CategoryForm,ProfileForm
from django.db.models import Q
from . forms import Registerform
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from . models import Profiles
from datetime import date

# Create your views here.

def calculate_price_adjustment(vehicle):
    current_year=date.today().year
    age=current_year - vehicle.manufacture_year
    distance=vehicle.distance_covered
    adjustment=(age * 1000) + (distance * 0.1)
    return adjustment



def home(request):
    allcategory=Category.objects.all()
    allvehicle=Vehicles.objects.all()
    return render(request,'home.html',{'categories':allcategory, 'allvehicle':allvehicle})

def about(request):
    return render(request,'about.html') 

def addvehicle(request):
    if request.method == 'POST':
        form=VehicleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(allvehicles)
    else:
        form=VehicleForm()
    return render(request,'addvehicles.html',{'form':form}) 


def vehicle_details(request,id):
    vehicle=Vehicles.objects.get(id=id)
    adjustment = calculate_price_adjustment(vehicle)
    adjusted_price = float(vehicle.base_price) - float(adjustment)
    return render(request,'vehiclelist.html',{'vehicle':vehicle,'adjusted_price':adjusted_price})

def allvehicles(request):
    allvehicle=Vehicles.objects.all()
    return render(request,'allvehicles.html',{'allvehicle':allvehicle})

def edit_vehicles(request,id):
    vehcle_update=Vehicles.objects.get(id=id)
    if request.method == 'POST':
        form=VehicleForm(request.POST,request.FILES,instance=vehcle_update)
        if form.is_valid():
            form.save()
            return redirect(allvehicles)
    else:
        form=VehicleForm(instance=vehcle_update)
    return render(request,'addvehicles.html',{'form':form}) 

def delete_vehcle(request,id):
    dlt_vehicle=Vehicles.objects.get(id=id)
    if request.method == 'POST':
        dlt_vehicle.delete()
        return redirect(allvehicles)
    return render(request,'confirm.html',{'dlt_vehicle':dlt_vehicle})

def addcategory(request):
    if request.method =='POST':
        form=CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(categorylist)
    else:
        form=CategoryForm()
    return render(request,'addcategory.html',{'form':form})

def categorylist(request):
    allcategory=Category.objects.all()
    return render(request,'categorylist.html',{'categories':allcategory})


def edit_category(request,name):
    updt_category=Category.objects.get(name=name)
    if request.method == 'POST':
        form=CategoryForm(request.POST,request.FILES,instance=updt_category)
        if form.is_valid():
            form.save()
            return redirect(categorylist)
    else:
        form=CategoryForm(instance=updt_category)
    return render(request,'addcategory.html',{'form':form})

def delete_category(request,name):
    dlt_category=Category.objects.get(name=name)
    if request.method =='POST':
        dlt_category.delete()
        return redirect(categorylist)
    return render(request,'confirm_delete.html',{'dlt_category':dlt_category})

def viewproduct(request,name):
    categor=Vehicles.objects.filter(category=name)
    return render(request,'category_vhicle.html',{'categor':categor})

def search_vehicle(request):
    a = ''
    if request.GET.get('search_this'):
        a=request.GET.get('search_this')
        print(a)

    allvehicle=Vehicles.objects.filter(
        Q(name__icontains=a) | Q(fuel_type__icontains=a) |Q(manufacture_year__icontains=a))
    return render(request,'allvehicles.html',{'allvehicle':allvehicle}) 

def register(request):
    if request.method=='POST':
        form=Registerform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User has been created')
            return redirect('login_page')
        else:
            messages.error(request,'Registration failed.Please correct the errors')
            print(form.errors)
            return render(request,'register.html',{'form':form})
    else:
        form=Registerform()
        return render(request,'register.html',{'form':form})

def welcome(request):
    return render(request,'welcome.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'User has been logged in')
            return redirect(welcome)
        else:
            messages.error(request,'Invalid Username or password')
            return redirect(register)

    return render(request,'loginpage.html')


@login_required(login_url='login_page')
def profile(request):
    user = request.user

    try:
        profile = Profiles.objects.get(user=user)
    except Profiles.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return render(request, 'profile_details.html', {'profile': profile})
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'addprofile.html', {'profile': profile, 'form': form})

def logoutpage(request):
    logout(request)
    messages.success(request,'User has been logged out')
    return redirect(home)


