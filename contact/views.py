from django.shortcuts import render


from django.shortcuts import render, redirect
from .forms import InquiryForm


def contact_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            return redirect('thank_you')
    else:
        form = InquiryForm()

    return render(request, 'contact/contact.html', {'form': form})
