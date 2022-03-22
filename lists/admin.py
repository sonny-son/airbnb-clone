from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    """List Admin Definition"""

    # 관리자 페이지 외부 리스트
    list_display = ("name", "user", "count_rooms")

    search_fields = ("name",)

    # 관리자 페이지 내부
    filter_horizontal = ("rooms",)
