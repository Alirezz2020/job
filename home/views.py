# home/views.py
from django.views.generic import ListView
from job.models import Job
from django.utils import timezone


class HomePageView(ListView):
    model = Job
    template_name = "home/home.html"  # the home template
    context_object_name = "jobs"
    paginate_by = 5  # adjust the number of jobs per page

    def get_queryset(self):
        qs = Job.objects.filter(
            deleted=False,  # assuming you have a deleted flag for history
            expiry_date__gt=timezone.now()
        ).order_by("-posted_at")  # order jobs by posted date descending

        # Filtering based on query parameters
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(title__icontains=q)

        country = self.request.GET.get("country")
        if country:
            qs = qs.filter(country__icontains=country)

        city = self.request.GET.get("city")
        if city:
            qs = qs.filter(city__icontains=city)

        # Optionally add filtering for category or subcategory if desired:
        category = self.request.GET.get("category")
        if category:
            qs = qs.filter(category__slug=category)
        subcategory = self.request.GET.get("subcategory")
        if subcategory:
            qs = qs.filter(subcategory__slug=subcategory)

        return qs
