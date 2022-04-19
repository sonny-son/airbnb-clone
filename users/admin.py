from django.contrib import admin

# 관리자페이지의 기본 user admin 패널 불러오기
from django.contrib.auth.admin import UserAdmin
from rooms import models as rooms_models
from . import models


class UserInline(admin.TabularInline):

    model = rooms_models.Room


# users.models에서 정의한 data가 관리자페이지에 반영될 수 있도록 models.User를 참조
# CustomUserAdmin은 User을 참조한 관리자페이지를 컨트롤하는 함수
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    # 관리자 페이지 외부 리스트
    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
        "email_verified",
        "email_secret",
        "login_method",
    )

    # 관리자 페이지 내부

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
                    "login_method",
                )
            },
        ),
    )

    inlines = (UserInline,)
