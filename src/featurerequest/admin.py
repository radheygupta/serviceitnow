from django.contrib import admin
from django import forms
from .models import Clients, Features, ProductArea


class ClientsModelForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'


class ClientsAdmin(admin.ModelAdmin):
    form = ClientsModelForm
    # list_display = ('title', 'published_date', 'news_paper')
    # list_filter = ['published_date']
    search_fields = ['name']


class ProductAreaModelForm(forms.ModelForm):
    class Meta:
        model = ProductArea
        fields = '__all__'


class ProductAreaAdmin(admin.ModelAdmin):
    form = ProductAreaModelForm
    search_fields = ['name']


class FeaturesModelForm(forms.ModelForm):
    class Meta:
        model = ProductArea
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class FeaturesAdmin(admin.ModelAdmin):
    form = ProductAreaModelForm
    list_display = ('title', 'client', 'priority', 'product_area', 'target_date')
    search_fields = ['name']


# admin.site.register(Clients, ClientsAdmin)
admin.site.register(Clients)
admin.site.register(ProductArea, ProductAreaAdmin)
admin.site.register(Features, FeaturesAdmin)
