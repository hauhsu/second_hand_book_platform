from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from basic.models import Book

# Create your views here.

def index(request):
    context = RequestContext(request)
    newest_books = Book.objects.order_by('shelf_date')[:5]
    context_dict = {
            'msg': 'Welcome!!',
            'newest_books': newest_books,
            }
    return render_to_response('basic/index.html', context_dict, context)
