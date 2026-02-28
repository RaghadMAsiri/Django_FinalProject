from django.shortcuts import render
from .models import Course, Category
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ContactForm  
# Create your views here.

# 1. Database-------------------------------------------------
def course_list(request):

    courses = Course.objects.all()
    
    context = {
        'courses': courses,
    }
    return render(request, 'courses/course_list.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            form.save() 
            clean_email = form.cleaned_data['email']
            send_email(request, clean_email)
            messages.success(request, 'تم إرسال رسالتك بنجاح! فريق TechHub سيتواصل معك قريباً.')
            return redirect('contact')
    else:
        form = ContactForm()
        
    return render(request, 'courses/contact.html', {'form': form})

def send_email(request,email):
    send_mail(
        ' TechHub ',
        'تم إرسال رسالتك بنجاح! فريق TechHub سيتواصل معك قريباً.',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False
    )
    
# 2. Sessions ---------------------------------------------------
def add_to_list(request, course_id):
    
    course = get_object_or_404(Course, id=course_id)
    
   
    cart = request.session.get('cart', {})
    course_id_str = str(course_id)

    
    if course_id_str in cart:
        messages.warning(request, 'هذه الدورة موجودة مسبقاً في قائمتك!')
    else:
        
        cart[course_id_str] = {
            'id': course.id,
            'title': course.title,
            'price': float(course.price),
        }
        
       
        request.session['cart'] = cart
        request.session['cart_counter'] = len(cart)
        request.session.modified = True
        
        messages.success(request, f'تمت إضافة "{course.title}" لقائمة التسجيل بنجاح')

    return redirect('course_list')

def my_list(request):
   
    cart = request.session.get('cart', {})
    
   
    total_price = sum(item['price'] for item in cart.values())
    
    context = {
        'cart': cart,
        'total_price': total_price
    }
    return render(request, 'courses/my_list.html', context)

# 3. Authentication ----------------------------------------
# 1. 
def auth_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            messages.success(request, 'تم إنشاء حسابك بنجاح!')
            return redirect("course_list")
    else:
        form = RegisterForm()
    return render(request, "courses/register.html", {"form": form})

# 2. 
def auth_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'أهلاً بك مجدداً {user.username}')
            
            
            next_url = request.GET.get('next', 'course_list')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, "courses/login.html", {"form": form})

# 3. 
def auth_logout(request):
    logout(request)
    messages.info(request, 'تم تسجيل الخروج بنجاح.')
    return redirect("course_list")

# 4. 
@login_required(login_url='login')
def checkout(request):
    
    request.session['cart'] = {}
    request.session['cart_counter'] = 0
    request.session.modified = True
    
    messages.success(request, 'تم تأكيد تسجيلك في الدورات بنجاح! سيتم التواصل معك قريباً.')
    return redirect('course_list')