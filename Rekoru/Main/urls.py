from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('', views.Index, name='IndexUrl'),
    path('accounts/', views.Accounts, name='AccountsUrl'),
    path('registration/', views.Registration, name='RegistrationUrl'),
    path('login/', views.Login, name='LoginUrl'),
    path('logout/', views.Logout, name='LogoutUrl'),
    path('catalog/', views.Catalog, name='Catalog'),
    path('addproject/', views.Addproject, name='AddprojectUrl')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
