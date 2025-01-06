# views.py
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q, Func, F, Value, CharField
from .models import Book

# ✅ SQL의 REPLACE를 사용하는 커스텀 ORM 함수
class RemoveSpaces(Func):
    function = 'REPLACE'
    template = "%(function)s(%(expressions)s, ' ', '')"
    output_field = CharField()

def index(request):
    query = request.GET.get('q', '').strip()
    books = Book.objects.all()
    
    # ✅ 검색어가 있을 경우 공백 제거 및 대소문자 무시 검색
    if query:
        query_no_space = query.replace(' ', '')

        # ✅ annotate로 임시 필드 생성 (공백 제거한 버전)
        books = books.annotate(
            title_no_space=RemoveSpaces(F('title')),
            author_no_space=RemoveSpaces(F('author'))
        ).filter(
            Q(title_no_space__icontains=query_no_space) |
            Q(author_no_space__icontains=query_no_space)
        )

    # ✅ 페이징 처리
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app/book_list.html', {
        'page_obj': page_obj,
        'query': query
    })
