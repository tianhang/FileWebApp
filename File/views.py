
from File.models import File
from File.forms import UploadFileForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
import os
from django.http import StreamingHttpResponse,HttpResponse


# Create your views here.

def filelist_with_form(request):
    file_list = File.objects.all()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UploadFileForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # handle_uploaded_file(request.FILES['file'])
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UploadFileForm()

    #return render(request, 'upload_page.html', {'form': form})
    return render(request,'file_list_page.html',{'files':file_list,'form': form})

def delete_file(request,pk):
    print pk
    File.objects.filter(id=pk).delete()
    return HttpResponseRedirect('/')


def detail_file(request,pk):
    file = File.objects.get(id=pk)
    return render(request,'file_detail_page.html',{'file':file})

def file_download(request,pk):
    file = File.objects.get(id=pk)
    #with open("/media/"+str(file.file),"rb") as f:
    file_path = settings.MEDIA_ROOT+"/"+str(file.file)
    with open(file_path, "rb") as f:
        c = f.read()
    return HttpResponse(c)


def big_file_download(request,pk):
    # do something...
    file = File.objects.get(id=pk)

    def file_iterator(file_name, chunk_size=512):
        with open(file_name,"rb") as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = settings.MEDIA_ROOT+"/"+str(file.file)
    #the_file_name = "hello.txt"

    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response

def update_filename(instance, filename):
    path = "upload/path/"
    format = instance.userid + instance.transaction_uuid + instance.file_extension
    return os.path.join(path, format)