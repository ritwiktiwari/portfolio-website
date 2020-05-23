from django.shortcuts import render
from .models import Job
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def index(request):
    jobs = Job.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(jobs, 6)
    page = request.GET.get('page')
    paged_jobs = paginator.get_page(page)
    context = {
        'jobs': paged_jobs,
    }
    return render(request, 'jobs/index.html', context)
