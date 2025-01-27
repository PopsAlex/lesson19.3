from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import Game, Buyer

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
    Buyers = Buyer.objects.all()
    print(Buyers)
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
            if password == repeat_password and int(age) >= 18 and username not in [i.name for i in Buyers]:
                context['username'] = f'Приветствуем, {username}!'
                Buyer.objects.create(name=username, age=age)
                return render(request, 'platform.html', context)
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in [i.name for i in Buyers]:
                info['error'] = 'Пользователь уже существует'
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'registration_page.html', info)
