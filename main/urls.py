from main.views import SalomView
from django.urls import path
from . import views
urlpatterns = [
    path('',views.SalomView.as_view(),name="salom")
]