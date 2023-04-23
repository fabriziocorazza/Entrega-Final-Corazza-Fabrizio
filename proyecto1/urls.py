"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from RedSocial.views import index, PostList, PostDetail, PostCreate, PostUpdate, PostDelete, SingUp, Login, Logout, ProfileUpdate, ProfileCreate, aboutme, MandarMensajes, VerMensajes, EliminarMensajes, DetailMensajes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="index"),
    path('admin/', admin.site.urls), 
    path("postseries/list", PostList.as_view(), name="post-list"),
    path("postseries/<pk>/detail", PostDetail.as_view(), name="post-detail"),
    path("postseries/create", PostCreate.as_view(), name="post-create"),
    path("postseries/<pk>/update", PostUpdate.as_view(), name="post-update"),
    path("postseries/<pk>/delete", PostDelete.as_view(), name="post-delete"),
    path("singup/", SingUp.as_view(), name="singup"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("profile/create", ProfileCreate.as_view(), name="profile-create"),
    path("profile/<pk>/update", ProfileUpdate.as_view(), name="profile-update"),
    path("abotme/",aboutme,name="aboutme"),
    path("mensajes/create", MandarMensajes.as_view(), name="mensajes-create"),
    path("mensajes/list", VerMensajes.as_view(), name="mensajes-list"),
    path("mensajes/<pk>/detail", DetailMensajes.as_view(), name="mensajes-detail"),
    path("mensajes/<pk>/delete", EliminarMensajes.as_view(), name="mensajes-delete"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)