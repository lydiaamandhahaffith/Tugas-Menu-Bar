from django.shortcuts import render
from . models import Dosen, Tenaga_Pendidik, Mahasiswa
# Create your views here.
def faperta(request):
    dosen = Dosen.objects.all()
    tenagaPendidik = Tenaga_Pendidik.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    context = {
        'dataDosen': dosen,
        'dataTenagaPendidik': tenagaPendidik,
        'dataMahasiswa': mahasiswa,
    }

    return render(request, 'indexfaperta.html', context)