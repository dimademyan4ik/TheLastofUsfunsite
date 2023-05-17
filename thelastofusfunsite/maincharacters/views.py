from django.shortcuts import render
from django.http import HttpResponse

def index(request): #1.Формируем функцию представления страницы maincharacters. В аргументах функции идет request-ссылка на HttpRequest(по ней доступна вся информации в рамках текущего о сессии  запроса , куках)
    return HttpResponse("Страница приложения maincharacters")
#2.Далее связываем функцию представления с соответсвующим url адресом
