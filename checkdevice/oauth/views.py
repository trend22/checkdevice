from django.shortcuts import render


def o_auth(request):
    return render(request, 'oAuth.html')
