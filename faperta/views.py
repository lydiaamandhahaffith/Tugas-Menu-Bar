from django.shortcuts import render
from . models import Dosen, Tenaga_Pendidik, Mahasiswa
from faperta.forms import FormMahasiswa, FormTenagaPendidik
from faperta.forms import FormDosen
from faperta.forms import FormTenagaPendidik
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