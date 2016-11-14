from lists import views
from django.conf.urls import url
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/the-only-list-in-the-world/$',
        views.view_list,
        name='view_list'),
    # url(r'^admin/', admin.site.urls),
]
