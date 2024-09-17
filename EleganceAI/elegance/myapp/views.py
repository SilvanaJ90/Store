
from django.shortcuts import render, get_object_or_404



def qa_admin(request):
    return render(request, 'qa_admin.html')
