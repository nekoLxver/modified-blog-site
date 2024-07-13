from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('all/', views.show_all, name='all'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.show_details, name='details'),
    path('share/<int:id>/', views.share_post, name='share'),
    path('delete/<int:id>/', views.delete_post, name='delete'),
    path('edit/<int:id>/', views.edit_post, name='edit'),
]
