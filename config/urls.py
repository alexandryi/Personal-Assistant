from django.contrib.auth import views as auth_views
from apps.users.views import register
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [

    path('admin/', admin.site.urls),

    path("", lambda request: redirect("/contacts/")),

    path(
        "contacts/",
        include("apps.contacts.urls")
    ),

    path('register/', register, name='register'),

    path(
        'accounts/login/',
        auth_views.LoginView.as_view(),
        name='login'
    ),

    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path('notes/', include('apps.notes.urls')),
    path('files/', include('apps.files.urls')),
    path('news/', include('apps.news.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)