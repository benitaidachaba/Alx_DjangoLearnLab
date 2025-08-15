from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path("books/", list_books, name="list_books"),  # FBV
    path("library/", LibraryDetailView.as_view(), name="library_detail"),
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('', views.home_view, name='home'),
    path('admin-only/', views.admin_view, name='admin_view'),
    path('librarian-only/', views.librarian_view, name='librarian_view'),
    path('member-only/', views.member_view, name='member_view'),
    path('add_book/', views.add_book_view, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book_view, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book_view, name='delete_book'),
]
