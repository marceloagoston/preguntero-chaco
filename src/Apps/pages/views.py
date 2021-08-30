from django.views.generic import TemplateView

from Apps.usuarios.models import Usuario

class HomePageView(TemplateView):
    template_name = 'home.html'

class AdminHomePageView(TemplateView):
    template_name = 'admin/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['usuariosRegistrados'] = Usuario.objects.all().count()

        return context