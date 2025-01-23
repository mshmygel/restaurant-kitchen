from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from accounts.models import Cook
from accounts.forms import (
    CookSearchForm,
    CookCreationForm,
    CookExperienceUpdateForm
)


# from django.contrib.auth.views import LoginView, LogoutView
# from django.urls import reverse_lazy
#
#
# class CustomLoginView(LoginView):
#     template_name = "registration/login.html"
#     redirect_authenticated_user = True
#     next_page = "/"
#     success_url = reverse_lazy("kitchen")
#
# class CustomLogoutView(LogoutView):
#     template_name = "registration/logged_out.html"
# from django.contrib.auth.views import LoginView, LogoutView
# from django.urls import reverse_lazy
#
# class CustomLoginView(LoginView):
#     template_name = "registration/login.html"
#     redirect_authenticated_user = True
#     success_url = reverse_lazy("kitchen")
#
# class CustomLogoutView(LogoutView):
#     template_name = "registration/logged_out.html"

class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "kitchen/cook_list.html"
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = CookSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Cook.objects.all()
        form = CookSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"])
        return queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "kitchen/cook_detail.html"
    queryset = Cook.objects.prefetch_related("dishes__dish_type")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    template_name = "kitchen/cook_form.html"
    form_class = CookCreationForm
    success_url = reverse_lazy("accounts:cook-list")


class CookExperienceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    template_name = "kitchen/cook_form.html"
    form_class = CookExperienceUpdateForm
    success_url = reverse_lazy("accounts:cook-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    template_name = "kitchen/cook_confirm_delete.html"
    success_url = reverse_lazy("accounts:cook-list")


