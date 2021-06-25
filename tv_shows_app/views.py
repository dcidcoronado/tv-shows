from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
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
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['date'],
        description = request.POST['description']
        )
        messages.success(request, 'Show succesfully created')   
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
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{show_id}/edit')
        else:
            show.title = request.POST['title']
            show.network = request.POST['network']
            show.release_date = request.POST['date']
            show.description = request.POST['description']
            show.save()
            messages.success(request, 'Show succesfully updated')        
            return redirect(f'/shows/{show_id}')


def destroy(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect ('/shows')


