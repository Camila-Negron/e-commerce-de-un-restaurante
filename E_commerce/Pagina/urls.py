from django.urls import path

from Pagina import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='Home'),
    path('blog', views.blog, name='Blog'),
    path('blogLeft', views.blogLeft, name='BlogLeft'),
    path('login', views.login, name='Login'),
    path('admin/', admin.site.urls, name='Admin'),
    path('nosotros', views.nosotros, name='Nosotros'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)