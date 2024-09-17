from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import *
from .forms import *
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import random
from datetime import datetime, timedelta


def members(request):
  M = Member.objects.all().order_by('-firstname').values()
  template = loader.get_template('member_names.html')
  context = {
    'M': M,
  }
  return HttpResponse(template.render(context,request))

def details(request, id):
  person = Member.objects.get(id=id)
  template = loader.get_template('member_details.html')
  context = {
    'person':person,
  }
  return HttpResponse(template.render(context, request))

def Employee_names(request):
  emp =Emp.objects.all().values()
  template =loader.get_template('emp_name.html')
  context={
    'Emp':emp
  }
  return HttpResponse(template.render(context,request))

def Employee_details(request,id):
  Employee=Emp.objects.get(id=id)
  template=loader.get_template('emp_details.html')
  context={
    'Emp':Employee
  }
  return HttpResponse(template.render(context,request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def form(request):
  template=loader.get_template('form.html')
  return HttpResponse(template.render({},request))

def addrecord(request):
  f=request.POST['Firstname']
  l=request.POST['Lastname']
  p=request.POST['Phone']
  s=request.POST['salary']
  po=request.POST['position']
  new=Emp(firstname=f,lastname=l,phone=p,salary=s,position=po)
  new.save()
  return HttpResponseRedirect(reverse('form'))

def contact(request):
   contacts=Contact.objects.all().values()
   context={
      'contacts':contacts
   }
   return render(request,'Contact_details.html',context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form=ContactForm()

    return render(request, 'contact_form.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def Members_view(request):
    if request.method == 'POST':
        form = MembersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form=MembersForm()

    return render(request, 'members_form.html', {'form': form})

def calculator_view(request):
    if 'result' not in request.session:
        request.session['result'] = 0

    if request.method == 'POST':
        value = int(request.POST.get('value'))
        operation = request.POST.get('operation')
      
        if operation == 'add':
            request.session['result'] += value
        elif operation == 'sub':
            request.session['result'] -= value
    
    template = loader.get_template('calc.html')
    context = {
        'result': request.session['result']
    }
    return HttpResponse(template.render(context, request))

def index(request):
    value_store,created = ValueStore.objects.get_or_create(id=1)
    
    if request.method == 'POST':
        form = ValueForm(request.POST)
        if form. is_valid():
            input_value = form.cleaned_data['input_value']
            if 'increment' in request.POST:
                value_store.value += input_value
            elif 'decrement' in request.POST:
                value_store.value -= input_value
            value_store.save()
            return redirect('index')
    else:
        form = ValueForm()
    
    context = {
        'form': form,
        'current_value': value_store.value,
    }
    return render(request, 'index.html', context)

def register(request):
      if request.method == 'POST':
         form = Register_form(request.POST)
         if form.is_valid():
            password=form.cleaned_data['password']
            confirm_password=form.cleaned_data['password_confirm']
            if password==confirm_password:
                 form.save()
            else:
                form.add_error('password_confirm',"paswords not match")
      else:
         form=Register_form()

      return render(request, 'register.html', {'form': form})

def login_r(request):
    if request.method == 'POST':
        form = Login_form(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            
            user = None
            if Register.objects.filter(username=username_or_email).exists():
                user = Register.objects.get(username=username_or_email)
            elif Register.objects.filter(email=username_or_email).exists():
                user = Register.objects.get(email=username_or_email)
            
            if user and password == user.password:
                new, created = USER.objects.get_or_create(id=1)
                new.username = user.username
                new.email = user.email
                new.password = user.password
                new.save()
                return redirect("dashboard")
            else:
                form.add_error(None, "Invalid username/email or password")
    else:
        form = Login_form()

    return render(request, 'login.html', {'form': form})

def dashboard(request):
    template = loader.get_template('dashboard.html')
    new, created = USER.objects.get_or_create(id=1)
    context = {
        'user': new
    }
    return HttpResponse(template.render(context, request))

def Names(request):
    if request.method == 'POST':
        form =EditDeleteForm(request.POST)
        if form.is_valid():
            form.save()     
    else:
        form =EditDeleteForm()
    
    data=name.objects.all().values()
    context={
        'form':form,
        'data':data,
        'Button':False
    }

    return render(request, 'Name.html',context)

def delete(request,id):
    x=name.objects.get(id=id)
    x.delete()
    return redirect('names')

def edit(request, id):
    Name= name.objects.get(id=id)
    if request.method == 'POST':
        form = EditDeleteForm(request.POST, instance=Name)
        if form.is_valid():
            form.save()
            return redirect('names')
    else:
        form = EditDeleteForm(instance=Name)
    
    context = {
        'form': form,
        'data': name.objects.all().values(),
        'Button':True
    }
    return render(request, 'Name.html', context)

def send_email_view(request):
    subject = 'Hello from Django!'
    message = 'This is a test email sent via Django.'
    sender = 'sujanpanda049@gmail.com'
    recipient_list = ['sujanpanda049@gmail.com',"vasapuvishal@gmail.com"]

    try:
        send_mail(
            subject, 
            message, 
            sender, 
            recipient_list,
            fail_silently=False,
            
        )
        return HttpResponse('Email sent successfully.')
    except Exception as e:
        return HttpResponse(f'An error occurred: {str(e)}', status=500)
    
def mail(request):
    if request.method == 'POST':
        form = emailform(request.POST)
        if form.is_valid():
            heading = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = 'sujanpanda049@gmail.com'
            recivers= form.cleaned_data['recipient_list']

            # Convert recipient_list to a list of email addresses
            recivers = [email.strip() for email in recivers.split(',')]

            try:
                send_mail(
                    heading,
                    message, 
                    sender, 
                    recivers
                )
                return HttpResponse(f'Emails  sent to {recivers} successfully.')
            except Exception as e:
                return HttpResponse(f'An error occurred: {str(e)}')
    else:
        form = emailform()

    return render(request, 'email.html', {'form': form})

otp_storage = {}

def generate_otp():
    return str(random.randint(100000, 999999))

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = generate_otp()
        otp_storage[email] = otp
        print(otp_storage.get(email))
        try:
            send_mail(
                'Your OTP Code',
                f'Your OTP code is {otp}',
                'sujanpanda049@gmail.com', 
                [email],
                fail_silently=False,
            )
            request.session['email'] = email
            print("otp=",otp)
            return redirect('verify_otp')
        except Exception as e:
            return HttpResponse(f'An error occurred: {str(e)}', status=500)

    return render(request, 'otp.html')

def register_email(request):
      if request.method == 'POST':
         form = Register_email_form(request.POST)
         if form.is_valid():
            password=form.cleaned_data['password']
            confirm_password=form.cleaned_data['password_confirm']
            if password==confirm_password:
                 form.save()
            else:
                form.add_error('password_confirm',"paswords not match")
      else:
         form=Register_email_form()

      return render(request, 'registration_email.html', {'form': form})

def login_email(request):
    if request.method == 'POST':
        form = Login_form(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            otp = generate_otp()
       
            user = None

            if Register_email.objects.filter(username=username_or_email).exists():
                user = Register_email.objects.get(username=username_or_email)
            elif Register_email.objects.filter(email=username_or_email).exists():
                user = Register_email.objects.get(email=username_or_email)

            if user and password == user.password:
                otp_storage[user.username] = {'otp':otp,'time':datetime.now()}
                try:
                    send_mail(
                        'Your OTP Code',
                        f'Your OTP code is {otp}',
                        'sujanpanda049@gmail.com',  
                        [user.email],
                        fail_silently=False,
                    )
                    request.session['username'] = user.username
                    print("otp=",otp)
                    print(otp_storage.get(user.username))
                    return redirect("verify_otp")
                except Exception as e:
                    return HttpResponse(f'An error occurred: {str(e)}', status=500)
            else:
                form.add_error(None, "Invalid username/email or password")
    else:
        form = Login_form()

    return render(request, 'login.html', {'form': form})

def verify_otp_view(request):
    if request.method == 'POST':
        user = request.session.get('username')
        otp = request.POST.get('otp')

        if user in otp_storage:
            stored_otp = otp_storage[user]['otp']
            otp_time = otp_storage[user]['time']
            if otp == stored_otp and datetime.now() - otp_time < timedelta(seconds=30):
                return HttpResponse(f'{user} you logged in successfully!')
            else:
                return redirect("login_email")
        else:
            return redirect("login_email")
    
        
    return render(request, 'verify_otp.html')

def login__view(request):
    if request.method == 'POST':
        form = Login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dash_board')
            else:
                form.add_error(None, "Invalid email or password")
    else:
        form = Login_form()
    return render(request, 'Login.html', {'form': form})

@login_required
def dash_board(request):
    return render(request,'dashboard.html')

def Product_register(request):
    if request.method == 'POST':
        form = product_Registration(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            panel = form.cleaned_data['panel']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['password_confirm']
            if panel == 'admin' and Product_user.objects.filter(email=email).exists():
                messages.info(request,'Email already exists as a user')
            elif panel == 'user' and Product_admin.objects.filter(email=email).exists():
                messages.info(request,'Email already exists as a admin')
            else:
                if password == confirm_password:
                    if panel == 'None':
                         messages.info(request,"choose correct panel")
                    elif panel == 'admin':
                        Product_admin.objects.create(username=username, email=email, password=password)
                    elif panel == 'user':
                        Product_user.objects.create(username=username, email=email, password=password)
                else:
                     messages.info(request,"passwords not matching")
        else:
            form.add_error(None, 'Invalid details provided')
    else:
        form = product_Registration()

    return render(request, "product_registration.html", {'form': form})


def Product_login(request):
    if request.method == 'POST':
        form = product_login(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            panel = form.cleaned_data['panel']
            user = None

            if panel == 'None':
                form.add_error(None, 'Select panel correctly')
            else:
                user_model = Product_admin if panel == 'admin' else Product_user
                if user_model.objects.filter(email=email, password=password).exists():
                    user = user_model.objects.get(email=email, password=password)
                    try:
                        otp = generate_otp()
                        otp_storage[user.username] = {'otp': otp, 'time': datetime.now()}
                        send_mail(
                            'Your OTP Code',
                            f'Your OTP code is {otp}',
                            'sujanpanda049@gmail.com',
                            [user.email],
                            fail_silently=False,
                        )
                        request.session['panel'] = panel
                        request.session['username'] = user.username
                        return redirect("verify_otp_product")
                    except Exception as e:
                        return HttpResponse(f'An error occurred: {str(e)}', status=500)
                else:
                    form.add_error(None, 'Invalid email/password')
        else:
            form.add_error(None, 'Invalid details')
    else:
        form = product_login()

    return render(request, "product_login.html", {'form': form})

def verify_otp_product(request):
    if request.method == 'POST':
        user = request.session.get('username')
        otp = request.POST.get('otp')

        if user in otp_storage:
            stored_otp = otp_storage[user]['otp']
            otp_time = otp_storage[user]['time']
            panel=request.session.get('panel')
            if otp == stored_otp and datetime.now() - otp_time < timedelta(seconds=30):
               if panel=='admin':
                   return redirect("product_admin")
               elif panel=='user':
                   return redirect("product_user")
        else:
            return redirect("product_login")
        
    return render(request, 'verify_otp.html')

def product_admin(request):
    if request.method == 'POST':
        form =Products_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            form.add_error(None, "Invalid email or password")
    else:
        form = Products_form()

    context = {
        'form': form,
        'Products': Product.objects.all().values(),
        'Button':False
    }
    return render(request, 'product_admin.html', context)

def delete_product(request,id):
    x=Product.objects.get(id=id)
    x.delete()
    return redirect('product_admin')
  
def edit_product(request, id):
    product= Product.objects.get(id=id)
    if request.method == 'POST':
        form = Products_form(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_admin')
    else:
        form = Products_form(instance=product)
    
    context = {
        'form': form,
        'Products': Product.objects.all().values(),
        'Button':True
    }
    return render(request,'product_admin.html',context)

def product_user(request):
    context = {
        'Products': Product.objects.all().values(),
    }
    return render(request, 'product_user.html', context)

def buy(request, id):
    if request.method == "POST":
        product=Product.objects.get(id=id)
        value = int(request.POST['buy_quantity'])
        if value > 0 and value <= product.quantity:
            product.quantity -= value
            product.save()
            return redirect('product_user')
        else:
            return redirect('product_user')

    return redirect('product_user')


def product_login_without_panel(request):
    if request.method == 'POST':
        form = Product_login_without_panel(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = None
            
            if Product_admin.objects.filter(email=email, password=password).exists():
                user = Product_admin.objects.get(email=email, password=password)
                user_type='admin'
            elif Product_user.objects.filter(email=email, password=password).exists():
                user = Product_user.objects.get(email=email, password=password)
                user_type='user'
            else:
                form.add_error(None, 'Invalid email/password')
            try:
                otp = generate_otp()
                otp_storage[user.username] = {'otp': otp, 'time': datetime.now(),'user_type':user_type}
                send_mail(
                    'Your OTP Code',
                    f'Your OTP code is {otp}',
                    'sujanpanda049@gmail.com',
                    [user.email],
                    fail_silently=False,
                )
                request.session['username'] = user.username
                return redirect("verify_otp_")
            except Exception as e:
                return HttpResponse(f'An error occurred: {str(e)}', status=500)
        else:
            form.add_error(None, 'Invalid details')
    else:
        form=Product_login_without_panel()
  
    return render(request, "login_product.html", {'form': form})

def verify_otp_(request):
    if request.method == 'POST':
        user = request.session.get('username')
        otp = request.POST.get('otp')

        if user in otp_storage:
            stored_otp = otp_storage[user]['otp']
            otp_time = otp_storage[user]['time']
            user_type=otp_storage[user]['user_type']
            if otp == stored_otp and datetime.now() - otp_time < timedelta(seconds=30):
               if user_type=='admin':
                   return redirect("product_admin")
               else:
                   return redirect("product_user")
        else:
            return redirect("product_login")
        
    return render(request, 'verify_otp.html')

def Quiz_Q(request):
    if request.method == 'POST':
        form =Questions_form(request.POST)
        if form.is_valid():
            Answer=form.cleaned_data['Answer']
            if Answer=='None':
                form.add_error(None,'select Answer correctly')
            else:
               form.save()
        else:
            form.add_error(None, "Invalid Question")
    else:
        form=Questions_form()

    context = {
        'form': form,
        'Questions': Quiz_questions.objects.all().values(),
    }
    return render(request, 'Quiz_question.html', context)

def delete_Question(request,id):
    x=Quiz_questions.objects.get(id=id)
    x.delete()
    return redirect('Quiz_Questions')

def Student_name(request):
    if request.method == 'POST':
        name=request.POST['Student_name']
        if name:
           request.session['name']=name 
           print(name)
           Quiz_type=request.POST['Quiz_type']
           if Quiz_type=='single':
               return redirect('Quiz_timer')
           else :
                return redirect('Quiz')

    return render(request,'Student_name.html')

def Quiz_page(request):
    correct_answers = 0
    name=request.session['name']
    if request.method == 'POST':  
        for i in range(Quiz_questions.objects.count() ):
            Question_id_key = f'question_id{i+1}'
            Answer_key = f'Answer{i+1}'
            if Question_id_key in request.POST and Answer_key in request.POST:
                Question_id = request.POST[Question_id_key]
                selected_answer = request.POST[Answer_key]
                if Quiz_questions.objects.filter(id=Question_id).exists():
                    Question = Quiz_questions.objects.get(id=Question_id)

                    if selected_answer == Question.Answer:
                        correct_answers += 1
                        
            else:
                continue
        marks=correct_answers
        context = {
            'Questions': Quiz_questions.objects.all(),
            'marks': marks,
            'name': name,
        }

        return render(request, 'Quiz_result.html', context)
    else:
        marks=None    

    context = {
        'Questions': Quiz_questions.objects.all().values(),
        'name':name,
        'marks':marks
    }
    return render(request, 'Quiz_page.html', context)

def Quiz_Timer(request):
    name = request.session.get('name', 'Guest')
    marks = 0
    questions = Quiz_questions.objects.all().count()

    if request.method == 'POST':
        for i in range(questions):
            selected_answer = request.POST.get(f'Answer{i+1}')
            correct_answer = Quiz_questions.objects.all()[i]
            if selected_answer == correct_answer.Answer:
                marks += 1

        context = {
            'Questions': Quiz_questions.objects.all(),
            'marks': marks,
            'name': name,
        }

        return render(request, 'Quiz_result.html', context)  

    context = {
        'Questions':Quiz_questions.objects.all(),
        'marks': marks,
        'name': name,
    }

    return render(request, 'Quiz_timer.html', context)





