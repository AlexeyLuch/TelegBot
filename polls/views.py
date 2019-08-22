from django.shortcuts import render
from .models import User_Name
from django.http import HttpResponse
from django.core.paginator import Paginator

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def users_check(request):
    user_sherch = User_Name.objects.all()
    # User_Name.objects.get_or_create(unique=user_agent,)
    paginator = Paginator(user_sherch, 2)  # Show 2 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'polls/support.html', {'contacts': contacts})
