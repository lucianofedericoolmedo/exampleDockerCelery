from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', views.login),
    path('api/sample_secure_without_perms', views.sample_secure_without_perms),
    path('api/sample_secure_garantizar', views.sample_secure_garantizar),
    path('api/alta_garantias', views.alta_garantias),
    path('api/actualizacion_garantias',views.actualizacion_garantias),
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

