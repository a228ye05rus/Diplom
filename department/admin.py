from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import Cathedra, Employee, Section, Article, TagNews, News
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    full_text = forms.CharField(label='Содержимое новости', widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'headline', 'date',)
    list_display_links = ('headline', )
    list_filter = ('date', )
    search_fields = ('headline', 'tag__name',)
    form = NewsAdminForm


class CathedraAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', )
    search_fields = ('name', )


class EmployeeAdminForm(forms.ModelForm):
    disciplines = forms.CharField(label='Преподаваемые дисцпилины', widget=CKEditorUploadingWidget())
    projects = forms.CharField(label='Проекты', widget=CKEditorUploadingWidget())
    publications = forms.CharField(label='Публикации', widget=CKEditorUploadingWidget())

    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeAdmin(admin.ModelAdmin):
    #, 'get_image'
    list_display = ('id', 'surname', 'name', 'midname')
    list_display_links = ('surname', 'name', 'midname')
    readonly_fields = ('get_image',)
    search_fields =('surname', 'name', 'midname')
    form = EmployeeAdminForm
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width="50" height="60"')

    get_image.short_description = "Фотография"


class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name',)


class ArticleAdminForm(forms.ModelForm):
    full_text = forms.CharField(label='Содержимое статьи', widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name', )
    form = ArticleAdminForm


class TagNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name', )


admin.site.register(Cathedra, CathedraAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(TagNews, TagNewsAdmin)
admin.site.register(News, NewsAdmin)
