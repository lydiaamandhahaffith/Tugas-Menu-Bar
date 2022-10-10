from django.contrib import admin
from . models import Dosen, Tenaga_Pendidik, Mahasiswa

# Register your models here.
admin.site.register(Dosen)
admin.site.register(Tenaga_Pendidik)
admin.site.register(Mahasiswa)