from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Book, Review, ReviewForm

# Create your views here.

def home(request):
    return render(request, 'book_rev_web/home.html')

def registerpage(request):
    return render(request, 'book_rev_web/register.html')

def loginpage(request):
    return render(request, 'book_rev_web/login.html')

def loggedhome(request):
    book_list = get_list_or_404(Book)
    return render(request, 'book_rev_web/loggedhome.html', {'books': book_list, 'username': request.user.username})

def details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    fixed_review = Review.objects.filter(book_id=book_id)
    users = []
    for fixrev in fixed_review:
        users.append(User.objects.get(id=fixrev.user_id))
    result = zip(users, fixed_review)
    return render(request, 'book_rev_web/bookdetails.html', {'book': book, 'result': result})

def log_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            book_list = get_list_or_404(Book)
            return render(request, 'book_rev_web/loggedhome.html',
                          {'books': book_list, 'username': request.user.username})
        else:
            return render(request, 'book_rev_web/login.html')
    elif request.method == 'POST':
        if request.user.is_authenticated:
            book_list = get_list_or_404(Book)
            return render(request, 'book_rev_web/loggedhome.html',
                          {'books': book_list, 'username': request.user.username})
        elif request.POST['username'] and request.POST['password']:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                book_list = get_list_or_404(Book)
                return render(request, 'book_rev_web/loggedhome.html',
                              {'books': book_list, 'username': request.user.username})
            else:
                return render(request, 'book_rev_web/login.html')
        else:
            return render(request, 'book_rev_web/login.html')

def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            book_list = get_list_or_404(Book)
            return render(request, 'book_rev_web/loggedhome.html',
                          {'books': book_list, 'username': request.user.username})
        else:
            return render(request, 'book_rev_web/register.html')
    elif request.method == 'POST':
        if request.user.is_authenticated:
            book_list = get_list_or_404(Book)
            return render(request, 'book_rev_web/loggedhome.html',
                          {'books': book_list, 'username': request.user.username})
        elif request.POST['username'] and request.POST['password'] and request.POST['fullname']:
            if User.objects.filter(username=request.POST['username']).exists():
                return render(request, 'book_rev_web/register.html')
            user = User.objects.create_user(request.POST['fullname'], None, request.POST['password'])
            user.username = request.POST['username']
            user.save()
            login(request, user)
            book_list = get_list_or_404(Book)
            return render(request, 'book_rev_web/loggedhome.html',
                          {'books': book_list, 'username': request.user.username})
        else:
            return render(request, 'book_rev_web/register.html')

def log_out(request):
    logout(request)
    return render(request, 'book_rev_web/home.html')

def postit(request, bookid):
    if request.method == 'GET':
        if request.user.is_authenticated:
            book_list = get_list_or_404(Book)
            return render(request, 'book_rev_web/loggedhome.html',
                          {'books': book_list, 'username': request.user.username})
        else:
            return render(request, 'book_rev_web/login.html')
    elif request.method == 'POST':
        if request.user.is_authenticated and request.POST['description']:
            review = ReviewForm(request.POST)
            if review.is_valid():
                instance = review.save(commit=False)
                instance.user = User.objects.get(pk=request.user.id)
                instance.book = Book.objects.get(pk=bookid)
                instance.save()
                book = get_object_or_404(Book, pk=bookid)
                fixed_review = Review.objects.filter(book_id=bookid)
                users = []
                for fixrev in fixed_review:
                    users.append(User.objects.get(id=fixrev.user_id))
                result = zip(users, fixed_review)
                return render(request, 'book_rev_web/bookdetails.html', {'book': book, 'result': result})
            else:
                book = get_object_or_404(Book, pk=bookid)
                fixed_review = Review.objects.filter(book_id=bookid)
                users = []
                for fixrev in fixed_review:
                    users.append(User.objects.get(id=fixrev.user_id))
                result = zip(users, fixed_review)
                return render(request, 'book_rev_web/bookdetails.html', {'book': book, 'result': result})
        else:
            book = get_object_or_404(Book, pk=bookid)
            fixed_review = Review.objects.filter(book_id=bookid)
            users = []
            for fixrev in fixed_review:
                users.append(User.objects.get(id=fixrev.user_id))
            result = zip(users, fixed_review)
            return render(request, 'book_rev_web/bookdetails.html', {'book': book, 'result': result})
    else:
        book = get_object_or_404(Book, pk=bookid)
        fixed_review = Review.objects.filter(book_id=bookid)
        users = []
        for fixrev in fixed_review:
            users.append(User.objects.get(id=fixrev.user_id))
        result = zip(users, fixed_review)
        return render(request, 'book_rev_web/bookdetails.html', {'book': book, 'result': result})




