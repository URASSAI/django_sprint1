from django.shortcuts import render


def about(request):
    """Функция обработчик запроса about."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Функция обработчик запроса rules."""
    template = 'pages/rules.html'
    return render(request, template)
