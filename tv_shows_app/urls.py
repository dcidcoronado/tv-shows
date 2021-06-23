from django.urls import path
from . import views


urlpatterns = [
    path('shows', views.index),
    path('', views.root),
    path('shows/new', views.new_show),
    path('shows/create', views.create_show),
    path('shows/<int:show_id>', views.show_detail),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows/<int:show_id>/update', views.edit_show),
    path('shows/<int:show_id>/destroy', views.destroy),
]
