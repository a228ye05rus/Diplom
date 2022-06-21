from django.urls import path
from . import views
from .views import SearchResultsView


urlpatterns = [
    path('', views.index, name='index'),
    path('search_news/', views.SearchResultsView.as_view(), name='search_news'),
    path('news', views.news_home, name='news_home'),
    path('news_details/<int:pk>', views.NewsDetail.as_view(), name='news_details'),
    path('article_details/<int:pk>', views.ArticleDetails.as_view(), name='article_details'),
    path('structure_cathedra/<int:id>/', views.CathedraDetails, name='structure_cathedra'),
    path('employee/<int:pk>', views.EmployeeDetail.as_view(), name='employee_details')
]
