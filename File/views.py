from django.shortcuts import render
from File.models import File
# Create your views here.

def filelist(request):
    file_list = File.objects.all()
    context = {'files':file_list}
    return render(request,'file_list_page.html',context)