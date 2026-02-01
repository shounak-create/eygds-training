from django.urls import path
from .views import contact_list, contact_edit, contact_delete

urlpatterns = [
    path("", contact_list, name="contact_list"),
    path("edit/<int:id>/", contact_edit, name="contact_edit"),
    path("delete/<int:id>/", contact_delete, name="contact_delete"),
]
