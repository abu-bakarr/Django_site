from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('admin/', admin.site.urls),
    # path('new-search/', views.new_search, name='new_search'),
]
