from django.shortcuts import redirect


def api_root_view(request):
    """Redirect root URL to Swagger documentation for better user experience"""
    return redirect('schema-swagger-ui')
