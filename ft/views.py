from django.shortcuts import render

from fkip.forms import FormDosen
from . models import Dosen, Tenaga_Pendidik, Mahasiswa
from ft.forms import FormMahasiswa
from ft.forms import FormDosen
from ft.forms import FormTenagaPendidik
# Create your views here.
def ft(request):
    dosen = Dosen.objects.all()
    tenagaPendidik = Tenaga_Pendidik.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    context = {
        'dataDosen': dosen,
        'dataTenagaPendidik': tenagaPendidik,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'indexft.html', context)

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
