from django.contrib import messages
from django.views.generic import TemplateView


class IndexView(TemplateView):

    def render_to_response(self, context, **response_kwargs):
        # messages.success(self.request, 'SUCCESS!!')
        return super().render_to_response(context, **response_kwargs)

