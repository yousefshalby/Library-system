from django.shortcuts import redirect, render, get_object_or_404
from .models import Books, Category
from .forms import BookForm, categoryForm
# Create your views here.

def home (request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_category = categoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    context ={
        'books':Books.objects.all(),
        'Categories':Category.objects.all(),
        'bookform' : BookForm(),
        'formcat':categoryForm(),
        'allbooks':Books.objects.filter(active=True).count(),
        'booksold':Books.objects.filter(status='sold').count(),
        'bookrenatal':Books.objects.filter(status='rental').count(),
        'bookavailable':Books.objects.filter(status='available').count(),

    }
    return render(request, 'books_layout.html', context)

def books (request):

    search = Books.objects.all()
    title = None
    if "search_name" in request.GET:
        title = request.GET["search_name"]
        if title:
            search = search.filter(title__icontains=title)

    context ={
        'Categories':Category.objects.all(),
        'books':search,
        'formcat':categoryForm(),

    }
    return render(request, 'books.html', context)    

def update (request, id):
    book_id = Books.objects.get(id =id)
    if request.method == 'POST':
        book_saved = BookForm(request.POST, request.FILES, instance = book_id)
        if book_saved.is_valid():
            book_saved.save()
            return redirect('/')    
    else:
        book_saved = BookForm(instance= book_id)

    context ={
        'form': book_saved
    }            

    return render(request, 'update.html', context)

def delete(request, id):
    book_deleted = get_object_or_404(Books, id=id)
    if request.method == 'POST':
        book_deleted.delete()
        return redirect('/')
    return render(request, 'delete.html') 
