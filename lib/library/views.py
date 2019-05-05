from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student, Book, History, Message
# Create your views here.


SUPER = 'admin'
PWD = '123'


def index(request):
    return render(request, 'library/index.html')


def login(request):
    return render(request, 'library/login.html')


def logins(request):
    return render(request, 'library/logins.html')


def logintool(request):
    if request.POST['username'] == SUPER and request.POST['password'] == PWD:
        return render(request, 'library/manager.html', {"g": SUPER})

    else:
        return render(request, 'library/login.html')


def books(request):
    book = Book.objects.all()
    return render(request, 'library/books.html', {'books': book})


def book(request, i):
    books = Book.objects.get(pk=i)
    return render(request, 'library/book.html', {'book': books})


def users(request):
    users = Student.objects.all()
    return render(request, 'library/users.html', {'users': users})


def modify(request, i):
    books = Book.objects.get(pk=i)
    return render(request, 'library/modify.html', {'book': books})


def judge(request):
    username = request.POST['username']
    password = request.POST['password']
    if password == Student.objects.all().filter(username=username)[0].password:
        i = Student.objects.all().filter(username=username)[0].id
        return HttpResponseRedirect('/lib/reader/%s/' % i)

    else:
        return HttpResponseRedirect('/lib/logins/')


def register(request):
    return render(request, 'library/register.html')


def register_tool(request):
    u = Student()
    is_ok = True
    for u in Student.objects.all():
        if request.POST['username'] == u.username:
            is_ok = False
    if request.POST['password'] == request.POST['password2'] and is_ok:
        u.username = request.POST['username']
        u.password = request.POST['password']
        if request.POST['college']:
            u.collage = request.POST['college']
        if request.POST['number']:
            u.num = request.POST['number']
        if request.POST['email']:
            u.email = request.POST['email']
        u.set_password(u.password)
        u.save()
        return HttpResponseRedirect('/lib/logins/')
    else:
        return HttpResponseRedirect('/lib/register/')


def logout(request):
    return HttpResponseRedirect('/lib/index/')


def query(request, i):
    u = Student.objects.get(pk=i)
    if request.method == 'GET':
        return render(request, 'library/reader_query.html', {"u": u})

    elif request.method == 'POST':
        f = request.POST['item']
        t = request.POST['query']
        if f == "name":
            books = Book.objects.all().filter(name__icontains=t)
        else:
            books = Book.objects.all().filter(author__icontains=t)
        print(books)
        return render(request, 'library/reader_query.html', {"u": u, 'books': books})


def info(request, i):
    u = Student.objects.get(pk=i)
    return render(request, 'library/reader_info.html', {"u": u})


def history(request, i):
    u = Student.objects.get(pk=i)
    h = History.objects.all().filter(user=u)
    return render(request, 'library/reader_histroy.html', {"h": h, "u":u})


def reader(request, i):
    u = Student.objects.get(pk=i)
    return render(request, 'library/reader.html', {'u': u})


def mod(request, i):
    u = Student.objects.get(pk=i)
    if request.method == 'GET':
        return render(request, 'library/reader_modify.html', {'u': u})
    if request.method == "POST":
        u.name = request.POST['username']
        u.email = request.POST['email']
        if not request.POST['password']:
            u.password = not request.POST['password']
        u.collage = request.POST['college']
        u.num = request.POST['number']
        u.save()
        return HttpResponseRedirect('/lib/info/%s/' % i, {'u': u})


def book_info(request, i, a):
    u = Student.objects.get(pk=a)
    if request.method == 'GET':
        b = Book.objects.get(pk=i)
        reader = History.objects.filter(book=b)
        if not len(reader) == 0:
            for r in reader:
                if r.statue:
                    reader = r
        else:
            reader = False

        return render(request, 'library/reader_book.html', {"book": b, 'reader': reader, 'u': u})
    else:
        h = History()
        h.user = Student.objects.get(pk=a)
        h.book = Book.objects.get(pk=i)
        h.statue = True
        h.save()
        b = Book.objects.get(pk=i)
        reader = h
        return render(request, 'library/reader_book.html', {"book": b, 'reader': reader, 'u':u})


def edit(request):
    if request.method == "GET":
        pass

    else:
        pass


def ajax(request):
    return reader(request, 'library/ajax.html')
