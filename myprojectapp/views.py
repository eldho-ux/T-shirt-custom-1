from .models import Product, TShirt
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TShirtForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


def cart(request):
    cart_ids = request.session.get('cart_items', [])
    print("Cart IDs in session:", cart_ids)

    cart_items = TShirt.objects.filter(id__in=cart_ids)
    total = sum(item.price for item in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })

def add_to_cart(request, tshirt_id):
    tshirt = get_object_or_404(TShirt, id=tshirt_id)

    cart = request.session.get('cart_items', [])
    if tshirt.id not in cart:
        cart.append(tshirt.id)
        request.session['cart_items'] = cart
        request.session.modified = True
    return redirect('cart')

def custom_tshirt(request):
    return render(request, 'custom_tshirt.html')


# crud

SIZE_PRICES = {
    'S': 300,
    'M': 350,
    'L': 400,
    'XL': 450,
}


def create_tshirt(request):
    if request.method == 'POST':
        form = TShirtForm(request.POST, request.FILES)
        if form.is_valid():
            tshirt = form.save(commit=False)



            # Dynamic pricing
            selected_size = form.cleaned_data['size']
            tshirt.price = SIZE_PRICES.get(selected_size, 299)  # default to 300 if not found
            tshirt.save()

            # Add to session cart
            cart = request.session.get('cart_items', [])
            cart.append(tshirt.id)  # save TShirt ID
            request.session['cart_items'] = cart
            request.session.modified = True
            request.session['last_created_tshirt'] = tshirt.id

            return redirect('tshirt_success')
        else:
            print("Form errors:", form.errors)

    else:
        form = TShirtForm()




    return render(request, 'create_tshirt.html', {'form': form})

#def tshirt_success(request):
 #   tshirt_id = request.session.get('last_created_tshirt')
  #  tshirt = TShirt.objects.get(id=tshirt_id) if tshirt_id else None
   # return render(request, 'tshirt_success.html', {'tshirt': tshirt})

# temporary

def coming_soon(request):
    return render(request,'soon')

def prototype_notice(request):
    form = NotificationForm(request.POST or None)
    submitted = False

    if request.method == 'POST' and form.is_valid():
        form.save()
        submitted = True

    return render(request, 'prototype.html', {'form': form, 'submitted': submitted})

#U


def edit_cart_item(request, tshirt_id):
    tshirt = get_object_or_404(TShirt, id=tshirt_id)

    if request.method == 'POST':
        form = TShirtForm(request.POST, request.FILES, instance=tshirt)
        if form.is_valid():
            form.save()
            return redirect('cart')
    else:
        form = TShirtForm(instance=tshirt)

    return render(request, 'edit_cart_item.html', {'form': form, 'tshirt': tshirt})

#D

def remove_from_cart(request, tshirt_id):
    cart = request.session.get('cart_items', [])
    if tshirt_id in cart:
        cart.remove(tshirt_id)
        request.session['cart_items'] = cart
        request.session.modified = True

    try:
        item = TShirt.objects.get(pk=tshirt_id)
        item.delete()
    except TShirt.DoesNotExist:
        pass

    return redirect('cart')

def delete_tshirt(request, tshirt_id):
    tshirt = get_object_or_404(TShirt, id=tshirt_id)
    tshirt.delete()

    cart = request.session.get('cart_items', [])
    if tshirt_id in cart:
        cart.remove(tshirt_id)
        request.session['cart_items'] = cart
        request.session.modified = True

    return redirect('home')