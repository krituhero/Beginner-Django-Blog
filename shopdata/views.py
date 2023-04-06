from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from shopdata.models import Contact, Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.views.generic import DetailView

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html' , {'posts' : posts})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def submitcontact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        haha = Contact(name=name, email=email, desc=desc)
        haha.save()
        messages.success(request, "You'r Message has been sent.")
    return render(request, 'contact.html')
    

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        
        if User.objects.filter(email=email).exists():


            """This is used to check if the same email user exists in the database
            if it does, just return a message saying this email exists or so. """


            messages.error(request, "This email is already registerd. Please type another email.")
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():

            messages.error(request, "This Username is already registerd. Please type another Username.")
            return render(request, 'signup.html')

        else:
            hehe = User.objects.create_user(username, email, password,)
            hehe.save()
            messages.success(request, "You have been successfully registered. Please Login To continue.")
            return redirect(loginuser)

    return render(request, 'signup.html')


def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        User = authenticate(request, username=username, password=password) 


        """This user above is just a random value, You can enter any value to authenticate the
        data entered and in the database"""


        if User is not None:
            login(request, User)
            messages.success(request, "Successfully Logged In.")
            return redirect('userpage')
        else:

            """Instead of http response here just generate a error message 
            saying invalid username or so"""

            messages.error(request, "Wrong Credentials. Please Enter again or Signup.")
            return render(request, 'login.html')

    return render(request, 'login.html')

@login_required
def userpage(request):
    posts = Post.objects.all()
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        # Get the uploaded file from the request
        image_file = request.FILES['image']
        if image_file is not None and 'image' in request.FILES and image_file.content_type.startswith('image/'):
            # Use the default Django storage backend to save the file
            filename = default_storage.save(image_file.name, ContentFile(image_file.read()))
            # Get the URL of the saved file
            image_url = default_storage.url(filename)
        else:
            image_url = None

        # filename = default_storage.save(image_file.name, ContentFile(image_file.read()))
        # image_url = default_storage.url(filename)

        if title and description:
            post = Post(title=title, description=description, author=request.user, image=image_url)
            post.save()
            messages.success(request, "Your Blog has been Successfully Updated.")
        else:
            messages.error(request, "Please fill the full form")

        return redirect("userpage")
    return render(request, 'userpage.html', {'posts' : posts})

@login_required
def userlogout(request):
    logout(request)
    messages.warning(request, "You have been Logged Out.")
    return redirect('index')

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author or request.user.is_superuser:
        post.delete()
    return redirect('userpage')

@login_required
def viewblog(request):
   posts = Post.objects.all()
   context ={'posts': posts}
   return render(request, 'blogpage.html', context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogpage.html'
    context_object_name = 'posts'

