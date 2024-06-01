from django.views.generic import TemplateView






# def messageview1 (request):
#     return render(request, 'home.html')

class Messageview(TemplateView):

    template_name = 'home.html'