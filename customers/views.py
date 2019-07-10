from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer

from django.utils import timezone
from .forms import CustomerForm, NewCustomerForm, EditCustomerForm

# Create your views here.

LOGIN_URL = '/' # redirect to this url when user is not authenticated, in our case, the home_page

@login_required(login_url=LOGIN_URL)
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/home.html', {'all_customers': customers })

@login_required(login_url=LOGIN_URL)
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(instance=customer)
    return render(request, 'customers/customer_detail.html', {'form' : form })

@login_required(login_url=LOGIN_URL)
def customer_new(request):
    if request.method == 'POST':
        form = NewCustomerForm(request.POST, initial={"contactName" : ''})

        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.date_created = timezone.now()
            customer.date_modified = timezone.now()
            customer.save()
            return redirect('customer_detail', pk=customer.pk)

    else:
        form = NewCustomerForm()

    return render(request, 'customers/customer_edit.html', {'form': form,
                                                            'title': 'New Customer',
                                                            })

@login_required(login_url=LOGIN_URL)
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = EditCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.date_modified = timezone.now()
            customer.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = EditCustomerForm(instance=customer)

    return render(request, 'customers/customer_edit.html', {'form' : form,
                                                            'title': 'Edit Customer',
                                                            })
