from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def val_email(request):
    text = request.GET['email']
    import re
    email_pat = re.compile(r"(\w+)@(\D{2,9}).(\w{2,9})")
    text1 = re.search(email_pat, text)
    return render(request, 'result.html', {'email':text1})