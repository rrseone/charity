from django.contrib import admin

from apps.charity.models import Role, Member, Social, Sponsor, City, SocialLink, OptionFile, OptionText, Testimonial, \
    HomeSlider, SiteSocialLink


class SocialLinkTabularInline(admin.TabularInline):
    model = SocialLink
    extra = 0
    fields = ('is_active', 'social', 'link')

@admin.register(SiteSocialLink)
class SiteSocialLinkAdmin(admin.ModelAdmin):
    pass

@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    pass

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

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass

@admin.register(OptionText)
class OptionTextAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'priority')
    list_editable = ('priority', 'value')

    fields = ('key', 'value', 'priority')
    readonly_fields = ('key',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(OptionFile)
class OptionFileAdmin(admin.ModelAdmin):
    list_display = ('key', 'caption', 'file', 'priority')
    list_editable = ('priority', 'caption', 'file')

    fields = ('key', 'caption', 'file', 'priority')
    readonly_fields = ('key',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
