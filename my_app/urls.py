from django.urls import path
from .views import Index, Profiles, delete_prof, update


urlpatterns = [
    path('', Index, name="index"),
    path('Profiles/', Profiles, name="Profiles"),
    path('delete_prof/<int:id>/', delete_prof, name='delete_prof'),
    path('update/<int:id>/', update, name='update'),
]