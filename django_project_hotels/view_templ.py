from django.views.generic.base import TemplateView
from django.views.generic.base import TemplateView

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from models import MyModel
from django.views.generic.edit import CreateView, FormView, DeleteView
from forms import MyModelForm, MyForm
from models import Comment
from django.urls import reverse_lazy


class MyModelDetailView(DetailView):
    model = MyModel
    template_name = 'my model_detail.html'
    context_object_name = 'object'

    class MyModelListView(ListView):
        model = MyModel
        template_name = 'my_model_list.html'
        context_object_name = 'objects'
        paginate_by = 10  # Количество объектов на странице
        queryset = MyModel.objects.filter(is_active=True)

        def get_queryset(self):
            # Фильтрация данных, если необходимо
            queryset = super().get_queryset()
            # Например, фильтрация по полю 'is_active'
            return queryset.filter(is_active=True)

    class MyModelCreateView(CreateView):
        form_class = MyModelForm
        template_name = 'my_model_form.html'
        success_url = '/success/'

    class MyFormView(FormView):
        form_class = MeForm
        template_name = 'my_form.html'
        success_url = '/success/'


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'
