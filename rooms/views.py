from math import ceil
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)  # url 에서 key : page인 정보를 가져온다.
    room_list = models.Room.objects.all()  # 리스트를 만든다.
    paginator = Paginator(room_list, 10, orphans=5)  # paginator은 모든 방과 관련된 정보를 가지고 있음
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")
