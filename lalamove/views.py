from django.shortcuts import render, redirect
from .models import Gender, Customer
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login,authenticate
from .models import tbl_Authentication
# Create your views here.
def index_gender(request):
    genders = Gender.objects.all() #select * from genders

    context = {
        'genders': genders
    }

    return render(request, 'gender/index.html', context)


def create_gender(request):
    return render(request, 'gender/create.html')

def store_gender(request):
    gender = request.POST.get('gender')
    Gender.objects.create(gender=gender) #insert into genders(gender) values(gender)
    messages.success(request, 'Gender successfully saved!')
    return redirect('/gender')

def show_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)  #select * from genders where gender_id = gender_id

    context = {
        'gender': gender,
    } 
    return render(request, 'gender/show.html', context)

def edit_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)  #select * from genders where gender_id = gender_id

    context = {
        'gender': gender,
    } 
    
    return render(request, 'gender/edit.html', context)

def update_gender(request, gender_id):
    gender = request.POST.get('gender')
    
    Gender.objects.filter(pk=gender_id).update(gender=gender) #update genders set gender = gender where gender_id = gender_id
    messages.success(request, 'Gender successsfully updated.')

    return redirect('/gender')

def delete_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)  #select * from genders where gender_id = gender_id

    context = {
        'gender': gender,
    } 
    
    return render(request, 'gender/delete.html', context)

def destroy_gender(request, gender_id):
    Gender.objects.filter(pk=gender_id).delete() # delete from genders where gender_id = gender_id
    messages.success(request, 'Gender successfully deleted.')

    return redirect('/gender')

def index_customer(request):
    customers = Customer.objects.select_related('gender')

    context = {
        'customers': customers,
    }

    return render(request, 'customer/index.html', context)

def create_customer(request):
    genders = Gender.objects.all() 

    context = {
        'genders': genders
    }

    return render(request, 'customer/create.html', context)

def store_customer(request):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    age = request.POST.get('age')
    genderId = request.POST.get('gender_id')
    birthDate = request.POST.get('birth_date')
    
    Customer.objects.create(first_name=firstName, middle_name=middleName, last_name=lastName, age=age, email=email, contact=contact,
    gender_id=genderId, birth_date=birthDate)
    messages.success(request, 'Customer successfully saved.')

    return redirect('/customers')
    
def show_customer(request, customer_id):
    customer = Customer.objects.get(pk=customer_id) 

    context = {
        'customer': customer,
    } 
    return render(request, 'customer/show.html', context)

def edit_customer(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)  #select * from genders where gender_id = gender_id
    genders = Gender.objects.all()

    context = {
        'genders': genders,
        'customer': customer,
    } 
    
    return render(request, 'customer/edit.html', context)

def update_customer(request, customer_id):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    age = request.POST.get('age')
    birthDate = request.POST.get('birth_date')
    genderID = request.POST.get('gender_id')

    Customer.objects.filter(pk=customer_id).update(first_name=firstName,middle_name=middleName,last_name=lastName,age=age, email=email, contact=contact, birth_date=birthDate,gender_id=genderID)
    messages.success(request, 'Customer successfully updated')
    
    return redirect('/customers')

def delete_customer(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)  #select * from genders where gender_id = gender_id

    context = {
        'customer': customer,
    } 
    
    return render(request, 'customer/delete.html', context)

def destroy_customer(request, customer_id):
    Customer.objects.filter(pk=customer_id).delete() # delete from genders where gender_id = gender_id
    messages.success(request, 'Customer successfully deleted.')

    return redirect('/customers')

def base(request):
        return render(request, 'base/base.html')
     
 
def user_login(request):
     
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
             
            try:
                user = tbl_Authentication.empAuth_objects.get(username=username,password=password)
                if user is not None:               
                    return render(request, 'create.html', {})
                else:
                    print("Someone tried to login and failed.")
                    print("They used username: {} and password: {}".format(username,password))
     
                    return redirect('/')
            except Exception as identifier:
                
                return redirect('/customers')
     
        else:
            return render(request, 'base/base.html')
        
def intro(request):
        return render(request, 'intro/intro.html')

def review(request):
        return render(request, 'review/review.html')
        
