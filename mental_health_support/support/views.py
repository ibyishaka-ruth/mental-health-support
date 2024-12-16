from django.shortcuts import render, redirect
from .models import Testimony, Photo, AISupport
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import requests  # Corrected import
from .forms import QuestionForm
from .models import Post
from django.http import JsonResponse


def home(request):
    testimonies = Testimony.objects.all()
    photos = Photo.objects.all()
    return render(request, 'support/home.html', {'testimonies': testimonies, 'photos': photos})

def about(request):
    return render(request, 'support/about.html')

def testimonies(request):
    testimonies = Testimony.objects.all()
    return render(request, 'support/testimonies.html', {'testimonies': testimonies})
def gallery(request):
    return render(request, 'support/gallery.html')  

def logout_view(request):
    logout(request)
    return redirect('login')
def faq(request):
    return render(request, 'support/faq.html')  

def contact_us(request):
    return render(request, 'support/contact.html')  

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('userdash')
        else:
            messages.error(request, "Invalid email or password!")
            return redirect('login')
    return render(request, 'support/login.html')

def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password == confirm_password:
            try:
                # Create the user
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()
                messages.success(request, 'Registration successful! You can now log in.')
                return redirect('login')  # Redirect to login page after successful registration
            except Exception as e:
                messages.error(request, f'Error creating user: {str(e)}')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'support/register.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()
                messages.success(request, 'Registration successful!')
                return redirect('login')  # Redirect to login page after successful registration
            except Exception as e:
                messages.error(request, f'Error: {str(e)}')
        else:
            messages.error(request, 'Passwords do not match.') 

    return render(request, 'support/register.html')

def dashboard(request):
    return render(request, 'support/userdash.html')

def chat_view(request):
    return render(request, 'support/chat.html')

def generate_answer(question):
    api_url = "https://api.openmentalhealth.org/your-endpoint"
    params = {'query': question}  # Corrected indentation
    # Add logic to call the API and process the response here
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            question = form.cleaned_data['question_text']
            # Do something with the question
    else:
        form = QuestionForm()

    return render(request, 'your_template.html', {'form': form})
def reflect(request):
    return render(request, 'support/reflect.html')  
def post(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'support/post.html', context)  
def save_post(request):
    post_text = request.POST.get('text')
    if post_text:
        post = Post.objects.create(user=request.user, text=post_text)
        post.save()
    return redirect('post')
def get_posts(request):
    posts = Post.objects.all()
    post_data = [{'user': {'username': post.user.username}, 'text': post.text} for post in posts]
    return JsonResponse(post_data, safe=False)
