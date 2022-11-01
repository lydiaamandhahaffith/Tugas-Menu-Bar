"""untirta URL Configuration

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
from faperta.views import faperta
from feb.views import feb
from fh.views import fh
from fisip.views import fisip
from fk.views import fk
from fkip.views import fkip
from ft.views import ft
from pascasarjana.views import pascasarjana
from profil.views import profil
from fkip.views import tambah_mahasiswa
from faperta.views import tambah_mahasiswa
from feb.views import tambah_mahasiswa
from fh.views import tambah_mahasiswa
from fisip.views import tambah_mahasiswa
from fk.views import tambah_mahasiswa
from ft.views import tambah_mahasiswa
from pascasarjana.views import tambah_mahasiswa
from faperta.views import tambah_dosen
from feb.views import tambah_dosen
from fh.views import tambah_dosen
from fisip.views import tambah_dosen
from fk.views import tambah_dosen
from fkip.views import tambah_dosen
from ft.views import tambah_dosen
from pascasarjana.views import tambah_dosen
from faperta.views import tambah_tendik
from feb.views import tambah_tendik
from fh.views import tambah_tendik
from fisip.views import tambah_tendik
from fk.views import tambah_tendik
from fkip.views import tambah_tendik
from ft.views import tambah_tendik
from pascasarjana.views import tambah_tendik
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faperta/', faperta),
    path('feb/', feb),
    path('fh/', fh),
    path('fisip/', fisip),
    path('fk/', fk),
    path('fkip/', fkip),
    path('ft/', ft),
    path('pascasarjana/', pascasarjana),
    path('profil/', profil),
    path('', views.index),
    path('tambah-mahasiswa/', tambah_mahasiswa),
    path('tambah-dosen/', tambah_dosen),
    path('tambah-tendik/', tambah_tendik),
]
