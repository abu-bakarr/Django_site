from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path('', views.index, name="index"),
    path('new_search/', views.new_search, name="search"),
    # path('^details/(?P<id>\d+)/$', views.details, name="index")
    # path('admin/', admin.site.urls),
    # path('new-search/', views.new_search, name='new_search'),
]
