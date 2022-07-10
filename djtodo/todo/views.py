from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView

from .forms import CreateForm
from .models import Task


# Create your views here.
class TodoCreate(CreateView):
    model = Task
    form_class = CreateForm
    template_name = "todo/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context


class Update(UpdateView):
    model = Task
    template_name = 'todo/update.html'
    success_url = "/"
    fields = {
        "title",
        "complete"
    }


class Delete(DeleteView):
    model = Task
    success_url = "/"
    template_name = 'todo/delete.html'
