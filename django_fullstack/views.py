from inertia import render

def welcome_page(request):
    """A welcome page for a successful project setup
    Args:
        request (HttpRequest): A valid http request

    Returns:
        httpResponse: An inertia render response
    """
    packages = ["Django"]
    return render(request, "index", {"packages": packages})
