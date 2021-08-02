from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('notes/',views.notes,name='notes'),
    path('delete-notes/<int:pk>',views.delete_notes,name="delete-note"),
    path('notesDetail/<int:pk>',views.NotesDetailView.as_view(),name="detail-note"),
    path('homework/',views.homework,name="homework"),
    path('update_homework/<int:pk>',views.update_homework,name="update_homework"),
    path('delete_homework/<int:pk>',views.delete_hoemwork,name="delete_homework"),
    path('youtube/',views.youtube,name="youtube"),
    path('todo/',views.todo,name="todo"),
    path('update_todo/<int:pk>',views.update_todo,name="update_todo"),
    path('delete_todo/<int:pk>', views.delete_todo, name="delete_todo"),
    path('book/', views.books, name="book"),
    path('dictionary/', views.dictionary, name="dictionary"),
    path('wiki/', views.wiki, name="wiki"),
    path('conver/', views.conversion, name="conversion"),
]