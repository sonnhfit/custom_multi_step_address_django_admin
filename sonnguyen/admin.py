from django.contrib import admin
from .models import Countries, Resorts, Tours
# Register your models here.

class ResortsInlineAdmin(admin.StackedInline):
    model = Resorts


@admin.register(Countries) 
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [ResortsInlineAdmin,]

@admin.register(Resorts)
class ResortsAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)
    search_fields = ('name',)


@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    change_form_template = 'admin/sonnguyen/add_form.html'
    list_display = ('country', 'resort',)
    # autocomplete_fields = ('country',)

    def add_view(self, request, form_url='', extra_context=None):
        # print('object id ======', object_id)
        extra_context = extra_context or {}
        extra_context['resort_to_country'] = Resorts.objects.all()
        return super().add_view(
            request, form_url, extra_context=extra_context,
        )

