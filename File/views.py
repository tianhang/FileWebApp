from django.shortcuts import render
from File.models import File
from File.forms import UploadFileForm
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def filelist(request):
    file_list = File.objects.all()
    context = {'files':file_list}
    return render(request,'file_list_page.html',context)

def filelist2(request):
    file_list = File.objects.all()
    #context = {'files':file_list}

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UploadFileForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # handle_uploaded_file(request.FILES['file'])
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/file/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UploadFileForm()

    #return render(request, 'upload_page.html', {'form': form})


    return render(request,'file_list_page.html',{'files':file_list,'form': form})


def upload_file(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UploadFileForm(request.POST,request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            #handle_uploaded_file(request.FILES['file'])
            form.save(  )
            # redirect to a new URL:
            return HttpResponseRedirect('/file/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UploadFileForm()

    return render(request, 'upload_page.html', {'form': form})

def handle_uploaded_file(f):
    with open('/media/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)