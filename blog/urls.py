from django.urls import path
from blog import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('blogs/', views.BlogList.as_view()),
    path('blogs/<int:blog_id>', views.BlogDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)