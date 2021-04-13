
from django.contrib import admin
from django.urls import path , include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from shit.views import shit_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('shit/' , include('shit.urls')),
    path('accounts/',include('accounts.urls')),
    path('',shit_list),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
