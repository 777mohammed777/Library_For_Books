from pickle import NONE
from django.shortcuts import render,redirect,get_object_or_404

from .models import *
from .forms import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        addbook =BookForm(request.POST, request.FILES)
        if addbook.is_valid():
            addbook.save()
            
        addcategory=CategoryForm(request.POST)
        if addcategory.is_valid():
            addcategory.save()
            
    context={'book':Book.objects.all(), 
             'category':Category.objects.all(),
             'form':BookForm(),
             'formcat':CategoryForm(),
             'all_books':Book.objects.filter(active = True).count(),
             'book_solid':Book.objects.filter(status ='sold').count(),
             'book_rental':Book.objects.filter(status ='rental').count(),
             'book_available':Book.objects.filter(status ='available').count(),
             }
    return render(request,'pages/index.html',context)
def books(request):
    search= Book.objects.all()
    
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)
            
    context={'books':search, 
             'category':Category.objects.all(),
             }
    return render(request,'pages/books.html',context)

def update(request,id):
    book_id = Book.objects.get(id=id)
    # context={'books':Book.objects.all(), 
    #          'category':Category.objects.all(),
    #          }
    if request.method == 'POST':
        book_form = BookForm(request.POST, request.FILES,instance=book_id)
        if book_form.is_valid():
            book_form.save()
            return redirect('/')
    else:
        book_form = BookForm(instance=book_id)
    
    context={
        'forms':book_form
    }

    return render(request,'pages/update.html',context)

def delete(request,id):
    book_delete = get_object_or_404(Book,id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request,'pages/delete.html')
