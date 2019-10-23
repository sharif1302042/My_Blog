from django.urls import path
from blog import views

urlpatterns = [
    path('home/', views.Index.as_view()),
]
