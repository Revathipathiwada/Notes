from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='/login/')
def editor(request):
    notes = Note.objects.filter(user=request.user)
    docid = request.GET.get('docid', None)

    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')

        if docid > 0:
            note = Note.objects.get(pk=docid, user=request.user)
            note.title = title
            note.content = content
            note.save()
            return redirect('editor')
        else:
            note = Note.objects.create(title=title, content=content, user=request.user)
            return redirect('editor')

    if docid:
        try:
            note = Note.objects.get(id=docid, user=request.user)
        except Note.DoesNotExist:
            note = None
    else:
        note = None

    context = {
        'notes': notes,
        'note': note,
        'docid': docid,
    }

    return render(request, 'editor.html', context)

@login_required(login_url='/login/')
def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content', '')
        Note.objects.create(title=title, content=content, user=request.user)
        return redirect('editor')

    return render(request, 'create_note.html')

@login_required(login_url='/login/')
def edit_note(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content', '')
        note.title = title
        note.content = content
        note.save()
        return redirect('editor')
    return render(request, 'create_note.html', {'note': note})

@login_required(login_url='/login/')
def delete_note(request, docid):
    note = get_object_or_404(Note, pk=docid, user=request.user)
    note.delete()
    return redirect('editor')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = authenticate(username=username, password=password)
        if user_obj is not None:
            login(request, user_obj)
            return redirect('editor')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, "login.html")

def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is taken")
            return redirect('register')
        user_obj = User.objects.create(username=username)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, "Account created")
        return redirect('login')
    return render(request, "register.html")

def custom_logout(request):
    logout(request)
    return redirect('login')
