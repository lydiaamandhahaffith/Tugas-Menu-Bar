from django.shortcuts import render
from . models import Dosen, Tenaga_Pendidik, Mahasiswa
from fkip.forms import FormDosen
from fkip.forms import FormMahasiswa
from fkip.forms import FormtenagaPendidik
# Create your views here.
def fkip(request):
    dosen = Dosen.objects.all()
    tenagaPendidik = Tenaga_Pendidik.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    context = {
        'dataDosen': dosen,
        'dataTenagaPendidik': tenagaPendidik,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'indexfkip.html', context)

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
        form = FormtenagaPendidik()
        context = {
            'form': form,
        }
        return render(request, 'tambah-tendik.html', context)