from django.shortcuts import render
from django.views.generic import View, ListView, FormView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import UserPassesTestMixin

def index(request):
    return render(request, 'base.html')


class LoginView(View):
    form_class = LoginForm
    template_name = 'login_page.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                HttpResponse('Invalid account')
        return render(request, self.template_name, {'form': form})
    

class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class FlowerList(ListView):
    model = Flower
    template_name = "flower_list.html"


class AddFlower(FormView):
    template_name = 'add_page.html'
    form_class = FlowerForm
    success_url = reverse_lazy('flowers')
    redirect_field_name = 'index'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateFlower(UpdateView):
    model = Flower
    template_name: str = "update_page.html"
    fields = [
        'name', 'price', 'quantity'
    ]
    success_url = reverse_lazy('flowers') 


class DeleteFlower(DeleteView):
    model = Flower
    template_name: str = 'delete_page.html'
    success_url = reverse_lazy('flowers') 


class MakeOrder(FormView):
    template_name = "add_page.html"
    form_class = OrderForm
    success_url = reverse_lazy('flowers')


    def form_valid(self, form):
        order = form.save(commit=False)
        order.customer = self.request.user
        order.flower = Flower.objects.get(pk=self.kwargs['pk'])
        if order.quantity > order.flower.quantity:
            form.add_error(None, 'Количество не может превышать кол-во цветов!')
            return super().form_invalid(form)
        print(Flower.objects.get(pk=self.kwargs['pk']))
        order.save()
        return super().form_valid(form)


class UpdateOrder():
    pass


class DeleteOrder():
    pass


class AdminOrderView(UserPassesTestMixin, ListView):
    model = Order
    template_name = "order_list.html"

    def test_func(self):
        return self.request.user.is_staff


class ProcessOrder(UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.is_staff

    def get(self, *args, **kwargs):
        Order.objects.get(pk=self.kwargs['pk']).execute_order()
        return HttpResponseRedirect(reverse('order_list')) 


class AddToFavorite(View):

    def get(self, *args, **kwargs):
        favorite = Favorite.objects.get_or_create(customer=self.request.user)[0]
        favorite_item = FavioriteItem.objects.create(favorite=favorite, item = Flower.objects.get(id=self.kwargs['pk']))
        return HttpResponseRedirect(reverse('profile')) 


class UserProfile(View):
    template_name = "my_profile.html"

    def get(self, request, *args, **kwargs):
        favorite = Favorite.objects.get_or_create(customer=request.user)[0]
        favorites = favorite.favorite_items.all()
        orders = Order.objects.filter(customer=request.user)
        return render(request, self.template_name, {'orders': orders, 'favorite_items': favorites})