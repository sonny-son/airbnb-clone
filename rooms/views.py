from django.views.generic import ListView
from django.shortcuts import render
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"


def room_detail(request, pk):

    return render(request, "rooms/detail.html")
