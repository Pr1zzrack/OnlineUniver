from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
]

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False)
]