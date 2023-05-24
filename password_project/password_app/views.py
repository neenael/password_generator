from django.views.generic import TemplateView
from .utils import create_password
from .forms import PasswordForm


class PasswordMake(TemplateView):
    template_name = 'password_app/general.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = PasswordForm(request.POST)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = PasswordForm(request.POST)
        if form.is_valid():
            context = self.get_context_data()
            context['form'] = form

            mode_dict = {
                "XKCD_password": "Словестный пароль",
                "common_password": "Символьный пароль",
            }
            complexity_dict = {
                "digit": "Только цифры",
                "digit_alpha": "Цифры и буквы",
                "complex": "Все символы",
            }
            mode = self.request.POST.get('mode')
            complexity = self.request.POST.get('complexity')
            length = self.request.POST.get('length')
            context["mode_dict"] = mode_dict.get(mode)
            context["complexity_dict"] = complexity_dict.get(complexity)
            context['password_result'] = create_password(length=length, mode=mode, complexity=complexity)
            return self.render_to_response(context)
