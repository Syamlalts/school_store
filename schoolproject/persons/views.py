from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Person, City


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirm')

        return render(request, 'home.html')

    return render(request, 'home.html', {'form': form})


def person_update_view(request, pk):

    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)

    return render(request, 'home.html', {'form': form})


# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)




def confirm(request):
    # if request.method == 'POST':
    #  username = request.POST['name']
    #
    # if User.objects.filter(username=username):
    #     messages.info(request, "Order Confirmed ")
    #     return render(request, 'confirm.html')
    return render(request,'confirm.html')



