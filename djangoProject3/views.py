from django.shortcuts import render


def rules_page(request):
    return render(request, "rules.html")


def establishments_page(request):
    return render(request, "establishments.html")
