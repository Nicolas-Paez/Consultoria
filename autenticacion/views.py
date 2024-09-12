from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
class Login(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('redireccionamiento')

    def form_valid(self, form):
        usuario = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if usuario is not None:
            login(self.request, usuario)
            return redirect(self.get_success_url())
        return super().form_valid(form)

class Redireccionamiento(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        usuario = self.request.user
        if usuario.rol == 'Administrador':
            return reverse_lazy('gestion_terapeutas')
        elif usuario.rol == 'Recepcionista':
            return reverse_lazy('listar_terapeutas_activos')
        elif usuario.rol == 'Terapeuta':
            return reverse_lazy('agenda')