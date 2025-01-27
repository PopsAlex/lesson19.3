from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import Game

# Create your views here.
def platform(request):
    title = 'Главная'
    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Корзина'
    context = {
        'title': title,
        'link1': link1,
        'link2': link2,
        'link3': link3,
    }
    return render(request, 'platform.html', context)


def games(request):
    Games = Game.objects.all()
    title = 'Игры'
    # game1 = f'{Game.title} | {Game.description}. Стоимость: {Game.cost}'
    button1 = 'Купить'
    button2 = 'Вернуться обратно'
    context = {
        'title': title,
        'games': Games,
        'button1': button1,
        'button2': button2,
    }
    return render(request, 'games.html', context)


def cart(request):
    title = 'Корзина'
    game = 'Извините, ваша корзина пуста'
    button = 'Вернуться обратно'
    context = {
        'title': title,
        'games': game,
        'button': button,
    }
    return render(request, 'cart.html', context)


def sign_up_by_django(request):
    title = 'Главная'
    context = {
        'title': title,
    }
    users = ['alex', 'pops', 'oleg', 'pomidor']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in users:
                context['username'] = f'Приветствуем, {username}!'
                return render(request, 'platform.html', context)
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'registration_page.html', info)


# def sign_up_by_html(request):
#     users = ['vasya', 'georgy', 'lenka', 'navuhodonosor']
#     info = {}
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         repeat_password = request.POST.get('repeat_password')
#         age = request.POST.get('age')
#         print('юзернаме', username)
#         print('пассворд', password)
#         print('репит пассворд', repeat_password)
#         print('возраст и тип', age, type(age))
#         if password == repeat_password and int(age) >= 18 and username not in users:
#             return HttpResponse(f'Приветствуем, {username}!')
#         elif password != repeat_password:
#             info['error'] = 'Пароли не совпадают'
#         elif int(age) < 18:
#             info['error'] = 'Вы должны быть старше 18'
#         elif username in users:
#             info['error'] = 'Пользователь уже существует'
#     return render(request, 'registration_page.html', info)