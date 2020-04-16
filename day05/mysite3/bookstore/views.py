import decimal

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Book


# Create your views here.

def all_book(request):
    all_book=Book.objects.filter(is_active=True)
    # all_book = Book.objects.all().order_by('id')
    # all_book=Book.objects.order_by()
    return render(request, 'bookstore/all_book.html', locals())


def update_book(request, book_id):
    try:
        book = Book.objects.get(id=int(book_id))
    except Exception as e:
        print("--get book is error--")
        print(e)
        return HttpResponse('--no book--')
    if request.method == 'GET':
        return render(request, 'bookstore/update_book.html', locals())
    elif request.method == 'POST':
        # 更新数据
        price = request.POST.get('price')
        market_price = request.POST.get('market_price')
        if not price or not market_price:
            return HttpResponse('---Please give me price or market_price')
        to_update=False
        if decimal.Decimal(price) != book.price:
            to_update=True
        if decimal.Decimal(market_price)!=book.market_price:
            to_update=True
        if to_update:
            print('-------to --- update------')
            book.price = price
            book.market_price = market_price
            book.save()
        return HttpResponseRedirect('/bookstore/all_book')

def delete_book(request,book_id):
    #伪删除
    books = Book.objects.filter(id=book_id,is_active=True)
    if not books:
        return HttpResponse('--no book--')
    book=books[0]
    book.is_active = False
    book.save()

    return HttpResponseRedirect( reverse('all_book'))