from django.shortcuts import render

# Create your views here.
def test_app(request):
    return render(request, 'testapp/test_app.html')