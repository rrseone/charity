from django.contrib import admin

from apps.base.models import Role, Member, Social, Sponsor, Option, City, SocialLink


class SocialLinkTabularInline(admin.TabularInline):
    model = SocialLink
    extra = 0
    fields = ('is_active', 'social', 'link')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    inlines = [SocialLinkTabularInline]


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    pass

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'priority')
    list_editable = ('priority', 'value')

    fields = ('key', 'value', 'priority')
    readonly_fields = ('key',)

    def has_add_permission(self, request):
        return False
