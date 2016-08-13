
from File.models import File
from File.forms import UploadFileForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.http import StreamingHttpResponse,HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def filelist_with_form(request):
    file_list = File.objects.all()
    paginator = Paginator(file_list, 7)  # Show 5 files per page
    page = request.GET.get('page')

    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        files = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        files = paginator.page(paginator.num_pages)


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
    return render(request,'file_list_page.html',{'files':files,'form': form})

def delete_file(request,pk):
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
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(str(file.file))

    return response
