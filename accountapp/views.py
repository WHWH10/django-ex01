from articleapp.models import Article
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.views.generic.list import MultipleObjectMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accountapp.forms import AccountUpdateForm
from accountapp.decorators import account_ownership_required

# Create your views here.
# feature/authentication

has_ownership = [account_ownership_required, login_required]

# Class Based View
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # resverse_lazy : Class Based View 사용함
    # reverse : Function Based View 사용함
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "accountapp/create.html"


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = "target_user"
    template_name = "accountapp/detail.html"

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(
            object_list=object_list, **kwargs
        )


# @method_decorator(login_required, "get")
# @method_decorator(login_required, "post")
# @method_decorator(account_ownership_required, "get")
# @method_decorator(account_ownership_required, "post")
@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = "target_user"
    form_class = AccountUpdateForm
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "accountapp/update.html"

    # User Authentication
    # self == view 의미한다(AccountUpdateView)
    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #         # return HttpResponseRedirect(reverse("accountapp:login"))

    # def post(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().post(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()


# @method_decorator(login_required, "get")
# @method_decorator(login_required, "post")
# @method_decorator(account_ownership_required, "get")
# @method_decorator(account_ownership_required, "post")
@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = "target_user"
    success_url = reverse_lazy("accountapp:login")
    template_name = "accountapp/delete.html"
