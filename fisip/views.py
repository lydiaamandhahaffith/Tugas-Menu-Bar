from django.shortcuts import render

from faperta.forms import FormDosen
from . models import Dosen, Tenaga_Pendidik, Mahasiswa
from fisip.forms import FormMahasiswa
from fisip.forms import FormTenagaPendidik
# Create your views here.
def fisip(request):
    dosen = Dosen.objects.all()
    tenagaPendidik = Tenaga_Pendidik.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    context = {
        'dataDosen': dosen,
        'dataTenagaPendidik': tenagaPendidik,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'indexfisip.html', context)

def tambah_mahasiswa(request):
        form = FormMahasiswa()
        context = {
            'form': form,
        }
        return render(request, 'tambah-mahasiswa.html', context)

def tambah_dosen(request):
        form = FormDosen()
        context = {
            'form': form,
        }
        return render(request, 'tambah-dosen.html', context)

def tambah_tendik(request):
        form = FormTenagaPendidik()
        context = {
            'form': form,
        }
        return render(request, 'tambah-tendik.html', context)
