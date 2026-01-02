from django.urls import path
from .views import add_member, list_member, remove_member

urlpatterns = [
    path('add/', add_member, name='add-member'),
    path('list/', list_member, name='list-member'),
    path('remove/<int:id>/', remove_member, name='remove-member'),
]
