from django.contrib import admin
from.models import Pages 
from django_grapesjs.admin import GrapesJsAdminMixin
from django import forms
# Register your models here.


class MyPagesForm(forms.ModelForm):
    class Meta:
        model = Pages
        fields = '__all__'


class PagesAdmin(GrapesJsAdminMixin, admin.ModelAdmin):
    form = MyPagesForm

    class Media:
        js = (
            'js/jquery.js',
            'js/popper.min.js',
            'js/bootstrap.min.js',
            'js/owl.js',
            'js/wow.js',
            'js/appear.js',
            'js/jquery.stellar.min.js',
            'js/jquery.fancybox.js',
            'js/mixitup.js',
            'js/jquery.mCustomScrollbar.concat.min.js',
            'js/swiper.min.js',
            'js/TweenMax.min.js',
            'js/script.js',
            'js/admin.js',
        )


@admin.register(Pages)
class PagesAdmin(PagesAdmin):
    pass