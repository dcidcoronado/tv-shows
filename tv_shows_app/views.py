from django.shortcuts import render, HttpResponse, redirect
from .models import Show

def root(request):
    return redirect('/shows')


def index(request):
    shows = Show.objects.all()
    context = {
        'shows': shows
    }
    return render(request, 'index.html', context)


def new_show(request):
    return render(request, 'new_show.html')


def create_show(request):    
    show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['date'],
        description = request.POST['description']
    )
    return redirect(f'/shows/{show.id}')


def show_detail(request, show_id):
    show = Show.objects.get(id=show_id)
    context = {
        'show': show
    }
    return render(request, 'show_detail.html', context)


def edit_show(request, show_id):
    show = Show.objects.get(id=show_id)
    if request.method == 'GET':
        context = {
            'show': show
        }
        return render(request, 'edit_show.html', context)
    elif request.method == 'POST':        
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['date']
        show.description = request.POST['description']
        show.save()        
        return redirect(f'/shows/{show_id}')


def destroy(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect ('/shows')


