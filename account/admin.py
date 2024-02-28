from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    empty_value_display = "--empty--"
    list_display = ("username","email")
    search_fields = ("username",)
    list_per_page = 100
    search_help_text = "search by ..."
    date_hierarchy = "date_joined"



    fieldsets = (
        (None, {"fields": ("username", "password")}),
		(_("Personal Info"), {"fields": ("first_name", "last_name", "email")}),
		(
			_("Permissions"),
			{
				"fields": (
					"is_active",
					"is_staff",
					"is_superuser",
					"groups",
					"user_permissions",
				),
			},
		),
		(_("Important dates"), {"fields": ("last_login", "date_joined")}),
	)
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2")
            }),
        )

