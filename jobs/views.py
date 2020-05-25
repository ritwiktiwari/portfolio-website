from django.shortcuts import render
from .models import Job
from photos.models import Photo
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    photos = Photo.objects.order_by('list_date').filter(is_published=True)
    jobs = Job.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(jobs, 6)
    page = request.GET.get('page')
    paged_jobs = paginator.get_page(page)
    context = {
        'jobs': paged_jobs,
        'photos': photos,
    }
    return render(request, 'jobs/index.html', context)
