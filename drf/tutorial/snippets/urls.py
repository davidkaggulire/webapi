from django.urls import path
from snippets import views

urlpatterns = [
    path('getsnippets/', views.get_snippets),
    path('addsnippets/', views.post_snippets),
    path('getsnippet/<int:pk>/', views.get_snippet),
    path('updatesnippet/<int:pk>/', views.update_snippet),
    path('deletesnippet/<int:pk>/', views.delete_snippet),
]