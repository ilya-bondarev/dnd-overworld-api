from django.http import HttpResponseNotFound
def common_handler_404(request, exception):
    return HttpResponseNotFound("<H1>Error 404</H1>");