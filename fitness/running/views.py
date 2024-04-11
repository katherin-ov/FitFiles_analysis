from django.shortcuts import render, redirect

from running.forms import UploadFileForm
from running.models import UploadFiles, Result
from running.parser import parse


hash_file = ""


def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
            global hash_file
            hash_file = parse(fp.file)
            return redirect('result')
    else:
        form = UploadFileForm()
    return render(request, 'running/index.html', {'form': form})


def result(request):
    results = Result.objects.all().filter(file_hash=hash_file)
    context = {
        'results': results,
    }
    return render(request, 'running/result.html', context)
