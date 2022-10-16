from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
class IndexView(TemplateView):
    template_name = 'index.html'


class DiaryCreateView(CreateView):
    template_name = 'diary_create.html'
    form_class = YujoBankForm
    success_url = reverse_lazy('yujobank:diary_create_complete')


class DiaryCreateCompleteView(TemplateView):
    template_name = 'diary_create_complete.html'


class DiaryListView(ListView):
    template_name = 'diary_list.html'
    model = YujoBank



class DiaryDetailView(DetailView):
    template_name = 'diary_detail.html'
    model = YujoBank


class DiaryUpdateView(UpdateView):
    template_name = 'diary_update.html'
    model = YujoBank
    fields = ('date', 'title', 'text',)
    success_url = reverse_lazy('yujobank:yujobank_list')

    def form_valid(self, form):
        YujoBank = form.save(commit=False)
        YujoBank.updated_at = timezone.now()
        YujoBank.save()
        return super().form_valid(form)


class DiaryDeleteView(DeleteView):
    template_name = 'diary_detele.html'
    model = YujoBank
    success_url = reverse_lazy('yujobank:yujobank_list')