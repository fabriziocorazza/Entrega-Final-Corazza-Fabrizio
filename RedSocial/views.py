from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from RedSocial.models import PostSeries, Profile, Mensajes
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    context = {
        "posts": PostSeries.objects.all()
        }
    return render(request, "RedSocial/index.html",context)

## Acerca de mi
def aboutme(request):
        return render(request, "RedSocial/aboutme.html")

## Posteos
class PostList(ListView):
    model = PostSeries

class PostDetail(DetailView):
    model = PostSeries

class PostCreate(LoginRequiredMixin, CreateView):
    model = PostSeries
    success_url = reverse_lazy("index")
    fields = ['Nombre_de_la_serie','Platamormas','Descripcion_de_la_serie','imagen']

    def  form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostSeries
    success_url = reverse_lazy("post-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return PostSeries.objects.filter(publisher=user_id, id=post_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, "RedSocial/not_found.html")


class PostDelete(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = PostSeries
    success_url = reverse_lazy("post-list")    
    
    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return PostSeries.objects.filter(publisher=user_id, id=post_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, "RedSocial/not_found.html")


## Singup LogIn LogOut
class SingUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/singup.html'
    success_url = reverse_lazy('index')

class Login(LoginView):
    next_page = reverse_lazy("index")

class Logout(LogoutView):
    template_name = 'registration/logout.html'


## Perfil
class ProfileCreate(CreateView):
    model = Profile
    fields = ['email','imagen']
    success_url = reverse_lazy('index')
    
    def  form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('index')


def base(request):
    context = {
        "perfiles": Profile.objects.all()
        }
    return render(request, "RedSocial/base.html",context)


## Mensaje
class MandarMensajes(CreateView):
    model = Mensajes
    fields = '__all__'
    success_url = reverse_lazy('index')

class VerMensajes(LoginRequiredMixin, ListView):
    model = Mensajes
    context_object_name = "mensajes"

    def get_queryset(self):
        return Mensajes.objects.filter(Destinatario=self.request.user.id).all()
    
class DetailMensajes(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Mensajes
    def test_func(self):
        user_id = self.request.user.id
        mensajes_id = self.kwargs.get('pk')
        return Mensajes.objects.filter(Destinatario=user_id).exists()

class EliminarMensajes(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensajes
    success_url = reverse_lazy("mensajes-list")
    
    def test_func(self):
        user_id = self.request.user.id
        mensajes_id = self.kwargs.get('pk')
        return Mensajes.objects.filter(Destinatario=user_id).exists()
    