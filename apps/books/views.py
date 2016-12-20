from django.views.generic import FormView
from apps.books.forms import BookCreateForm


class CreateFormView(FormView):
    template_name = "books/create.html"
    form_class = BookCreateForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(CreateFormView, self).form_valid(form)
