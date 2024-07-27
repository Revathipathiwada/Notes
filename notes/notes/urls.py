from django.contrib import admin
from django.urls import path
from document import views 

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.custom_logout, name='logout'),
    path('', views.editor, name='editor'),
    path('create_note/', views.create_note, name='create_note'),
    path('edit_note/<int:id>/', views.edit_note, name='edit_note'),
    path('delete_note/<int:docid>/', views.delete_note, name='delete_note'),
    path('admin/', admin.site.urls),
]
