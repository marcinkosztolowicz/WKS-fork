from django.contrib import admin
from django.contrib.auth.models import User

from import_export.admin import ImportExportModelAdmin
from import_export import resources

from apps.user.models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "userprofiles"


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        import_id_fields = ("email",)
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "id",
        )


class UserAdmin(ImportExportModelAdmin):
    resource_classes = [UserResource]
    inlines = [UserProfileInline]


class UserProfileResource(resources.ModelResource):
    class Meta:
        model = UserProfile
        import_id_fields = ("user",)
        fields = (
            "fund",
            "phone_number",
            "user",
            "koop_id",
        )


class UserProfileAdmin(ImportExportModelAdmin):
    resource_classes = [UserProfileResource]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
