# job/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Job, Category, SubCategory
from django.utils import timezone

class JobListView(ListView):
    model = Job
    template_name = "job/job_list.html"
    context_object_name = "jobs"
    paginate_by = 10

    def get_queryset(self):
        qs = Job.objects.filter(deleted=False, expiry_date__gt=timezone.now())
        qs = qs.order_by("-posted_at")
        # Advanced filtering: use GET parameters:
        category = self.request.GET.get('category')
        subcategory = self.request.GET.get('subcategory')
        country = self.request.GET.get('country')
        city = self.request.GET.get('city')
        if category:
            qs = qs.filter(category__slug=category)
        if subcategory:
            qs = qs.filter(subcategory__slug=subcategory)
        if country:
            qs = qs.filter(country__code=country)  # adjust field lookup as needed
        if city:
            qs = qs.filter(city__id=city)
        return qs

class JobDetailView(DetailView):
    model = Job
    template_name = "job/job_detail.html"
    context_object_name = "job"

class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['title', 'description', 'category', 'subcategory', 'country', 'city', 'job_type']
    template_name = "job/job_form.html"

    def form_valid(self, form):
        form.instance.employer = self.request.user
        # (Optional) enforce posting limits, permissions, etc.
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('job:job_detail', kwargs={'pk': self.object.pk})

class JobUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Job
    fields = ['title', 'description', 'category', 'subcategory', 'country', 'city', 'job_type']
    template_name = "job/job_form.html"
    permission_required = 'job.change_job'

    def get_queryset(self):
        return Job.objects.filter(employer=self.request.user)

    def get_success_url(self):
        return reverse_lazy('job:job_detail', kwargs={'pk': self.object.pk})
class JobDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        job = get_object_or_404(Job, id=pk, employer=request.user)
        job.deleted = True
        job.save()
        messages.success(request, "Job moved to history.")
        return redirect("job:dashboard")

class EmployerDashboardView(LoginRequiredMixin, ListView):
    template_name = "job/dashboard.html"
    context_object_name = "active_jobs"

    def get_queryset(self):
        # Active jobs are not deleted and not expired
        return Job.objects.filter(employer=self.request.user, deleted=False, expiry_date__gt=timezone.now())
