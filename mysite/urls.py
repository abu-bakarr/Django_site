from django.contrib import admin
from django.urls import path, include
from polls import views

urlpatterns = [
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
    # path('new-search/', views.new_search, name='new_search'),

]
