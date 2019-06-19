from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import DetailView

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/<int:pk_year>/<int:pk_type>', views.list_type, name='list_type'),
    path('list/<int:pk_year>', views.list_year, name='list_year'),
    path('show/<int:pk_report>', views.show_report, name='show'),
    path('add/', login_required(views.add_report), name='add'),
]