from django.shortcuts import render, get_object_or_404
from .models import Section, Article, News, Cathedra, Employee
from django.views.generic import DetailView, TemplateView, ListView
from django.db.models import Q


class SearchResultsView(ListView):
    """Поиск новостей"""
    def get_queryset(self):
        return News.objects.filter(headline__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context


def index(request):
    cath = Cathedra.objects.all()
    sect = Section.objects.all()
    return render(request, 'department/index.html', {'sects': sect, 'caths': cath})


def news_home(request):
    news = News.objects.order_by('-date')
    sect = Section.objects.all()

    return render(request, 'department/news_home.html', {'sects': sect, 'news': news})


class NewsDetail(DetailView):
    model = News
    template_name = 'department/news_details.html'
    context_object_name = 'news'


class ArticleDetails(DetailView):
    model = Article
    template_name = 'department/article_details.html'
    context_object_name = 'article'


def CathedraDetails(request, id):
    cathedra = get_object_or_404(Cathedra, id=id)
    name_cath = cathedra.name
    employee = Employee.objects.filter(cathedra=cathedra)

    context = {'cathedra': cathedra, 'employee': employee, 'name': name_cath}
    return render(request, 'department/structure_cathedra.html', context)


class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'department/employee_details.html'
    context_object_name = 'employee'
