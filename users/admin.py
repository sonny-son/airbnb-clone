from django.contrib import admin

# 관리자페이지의 기본 user admin 패널 불러오기
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.

# users.models에서 정의한 data가 관리자페이지에 반영될 수 있도록 models.User를 참조
# CustomUserAdmin은 User을 참조한 관리자페이지를 컨트롤하는 함수
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    # UserAdmin은 fieldset 블럭으로 구분됨
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
