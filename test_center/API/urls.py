from django.urls import path
from . import views


app_name = "API"
urlpatterns = [
    path('', views.answer_list),
    path('authentication/', views.authentication),
]
