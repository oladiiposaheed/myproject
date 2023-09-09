from django.shortcuts import render
from testapp.forms import FeedbackForm
# Create your views here.

def feedback_view(request):
    submitted = False
    name = ''
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print('Form Validation success')
            print('Name:',form.cleaned_data['name'])
            print('Userame:',form.cleaned_data['username'])
            submitted = True
            name = form.cleaned_data['name']

    print('Some Field Validation Fails')
    #form = FeedbackForm()
    return render(request, 'testapp/form6.html', {'form': form, 'name': name, 'submitted': submitted})
