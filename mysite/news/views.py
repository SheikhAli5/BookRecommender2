from django.shortcuts import render
from django.http import HttpResponse

from .models import News
from .models import Users



def index(request):
    news = News.objects.all()

    return render(request, 'news/index.html', {'news': news, 'title': 'Опрос'})

def createpost(request):
    if request.method == 'POST':
        if request.POST.get('firstname') and request.POST.get('lastname'):
            user = Users()
            user.firstname = request.POST.get('firstname')
            user.lastname = request.POST.get('lastname')
            user.save()

            return render(request, 'news/templates/news/index.html')

    else:
        return render(request, 'news/templates/news/index.html')