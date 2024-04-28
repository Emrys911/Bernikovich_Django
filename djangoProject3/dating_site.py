import os
from django.shortcuts import render


def rules_page(request):
    return render(request, "rules.html")


def establishments_page(request):
    return render(request, "establishments.html")
def split_path(path):
    return os.path.split(path)


def join_path(*args):
    return os.path.join(*args)


def views():
    pass