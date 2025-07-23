from decimal import Decimal
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import *

def add_pc_view(request: HttpRequest):
    if request.method == "POST":
        new_pc = PC(
            name=request.POST["name"],
            cpu=request.POST["cpu"],
            gpu=request.POST["gpu"],
            ram=request.POST["ram"],
            storage=request.POST["storage"],
            price=request.POST["price"],
            image=request.FILES["image"],
        )
        new_pc.save()
        return redirect('main:home_view')
    
    return render(request, "store/add_pc.html")


def add_product_view(request: HttpRequest):
    products = [
    {"name": "PC", "url_name": "store:admin_pc_view", "image_url": "/static/images/Products/PC.png"},
    {"name": "Monitor", "url_name": "store:admin_monitor_view", "image_url": "/static/images/Products/monitor.png"},
    {"name": "Keyboard", "url_name": "store:admin_keyboard_view", "image_url": "/static/images/Products/keyboard.png"},
    {"name": "Headset", "url_name": "store:admin_headset_view", "image_url": "/static/images/Products/headset.png"},
    {"name": "Mouse", "url_name": "store:admin_mouse_view", "image_url": "/static/images/Products/mouse.png"},
    {"name": "Gaming Chair", "url_name": "store:admin_chair_view", "image_url": "/static/images/Products/chair.png"},
    ]

    return render(request, "store/add_product.html", {"products": products})



def pc_detail_view(request: HttpRequest , pc_id :int):
     
    pc = PC.objects.get(pk=pc_id)

    pcs = PC.objects.filter(category=pc.category).exclude(pk=pc.id)[0:6]
   
    comments = PC_comment.objects.filter(pc=pc)

    return render(request, "store/pc_detail.html", {"pc" : pc , "pcs" : pcs , "comments" : comments})

    

def update_pc_view(request: HttpRequest, pc_id: int):

    pc = PC.objects.get(pk=pc_id)

    if request.method == "POST":
        pc.name=request.POST["name"]
        pc.cpu=request.POST["cpu"]
        pc.gpu=request.POST["gpu"]
        pc.ram=request.POST["ram"]
        pc.storage=request.POST["storage"]
        pc.price=request.POST["price"]
        pc.price = Decimal(request.POST["price"])

        if "image" in request.FILES : pc.image = request.FILES["image"]
        
        pc.save()
        
        return redirect('store:pc_detail_view' , pc_id = pc.id)
    
    return render(request, "store/update_pc.html", {"pc": pc})


def delete_pc_view(request: HttpRequest , pc_id: int):

    pc = PC.objects.get(pk=pc_id)

    pc.delete()
    return redirect('main:home_view')

def delete_monitor_view(request: HttpRequest , monitor_id: int):

    monitor = Monitor.objects.get(pk=monitor_id)

    monitor.delete()
    return redirect('main:home_view')

def display_all_view(request: HttpRequest):
    pcs = PC.objects.all()
    monitors  = Monitor.objects.all()
    mouses  = Mouse.objects.all()
    chairs  = Chair.objects.all()
    headsets  = Headset.objects.all()
    keyboards  = Keyboard.objects.all()

    return render(request, "store/display_all.html", {
        "pcs" : pcs , 
        "monitors" : monitors , 
        "mouses" : mouses , 
        "chairs" : chairs,
        "headsets" : headsets,
        "keyboards" : keyboards,
        })
    
    
    
def add_monitor_view(request: HttpRequest):
    if request.method == "POST":
        new_monitor = Monitor(
            name=request.POST["name"],
            size_in_inches=request.POST["size_in_inches"],
            resolution=request.POST["resolution"],
            refresh_rate=request.POST["refresh_rate"],
            price=Decimal(request.POST["price"]),
            image=request.FILES["image"],
        )
        new_monitor.save()
        return redirect('main:home_view')
    
    return render(request, "store/add_monitor.html")

def update_monitor_view(request: HttpRequest, monitor_id: int):
    monitor = Monitor.objects.get( pk=monitor_id)

    if request.method == "POST":
        monitor.name = request.POST["name"]
        monitor.size_in_inches = request.POST["size_in_inches"]
        monitor.resolution = request.POST["resolution"]
        monitor.refresh_rate = request.POST["refresh_rate"]
        monitor.price = Decimal(request.POST["price"])

        if "image" in request.FILES:
            monitor.image = request.FILES["image"]
        
        monitor.save()

        return redirect('store:monitor_detail_view', monitor_id=monitor.id)
    
    return render(request, "store/update_monitor.html", {"monitor": monitor})

def monitor_detail_view(request: HttpRequest , monitor_id :int):
    monitor = Monitor.objects.get(pk=monitor_id)
    monitors = Monitor.objects.filter(category=monitor.category).exclude(pk=monitor.id)[0:6]
    comments = Monitor_comment.objects.filter(monitor=monitor)

    return render(request, "store/monitor_detail.html", {"monitor" : monitor , "monitors" : monitors , "comments" : comments})


def add_mouse_view(request: HttpRequest):
    if request.method == "POST":
        new_mouse = Mouse(
            name=request.POST["name"],
            dpi=request.POST["dpi"],
            connection_type=request.POST["connection_type"],
            price=request.POST["price"],
            image=request.FILES["image"],
        )
        new_mouse.save()
        return redirect('main:home_view')
    
    return render(request, "store/add_mouse.html")
   
def delete_mouse_view(request: HttpRequest , mouse_id: int):

    mouse = Mouse.objects.get(pk=mouse_id)

    mouse.delete()
    return redirect('main:home_view')


def mouse_detail_view(request: HttpRequest , mouse_id :int):
    mouse = Mouse.objects.get(pk=mouse_id)
    comments = Mouse_comment.objects.filter(mouse=mouse)
    mouses = Mouse.objects.filter(category=mouse.category).exclude(pk=mouse.id)[0:6]

    return render(request, "store/mouse_detail.html", {"mouse" : mouse , "mouses" : mouses , "comments" : comments })

def update_mouse_view(request: HttpRequest, mouse_id: int):
    mouse = Mouse.objects.get(pk=mouse_id)

    if request.method == "POST":
        mouse.name=request.POST["name"]
        mouse.dpi=request.POST["dpi"]
        mouse.connection_type=request.POST["connection_type"]
        mouse.price=request.POST["price"]
        
        if "image" in request.FILES:
            mouse.image = request.FILES["image"]
        
        mouse.save()
        
        return redirect('store:mouse_detail_view', mouse_id=mouse.id)
    
    return render(request, "store/update_mouse.html", {"mouse": mouse})

def add_chair_view(request: HttpRequest):
    if request.method == "POST":
        new_chair = Chair(
            name=request.POST["name"],
            color=request.POST["color"],
            material=request.POST["material"],
            adjustable=request.POST["adjustable"],
            max_weight=request.POST["max_weight"],
            price=request.POST["price"],
            image=request.FILES["image"],
        )
        new_chair.save()
        return redirect('main:home_view')

    return render(request, "store/add_chair.html")

def chair_detail_view(request: HttpRequest , chair_id :int):
    chair = Chair.objects.get(pk=chair_id)
    comments = Chair_comment.objects.filter(chair=chair)
    chairs = Chair.objects.filter(category=chair.category).exclude(pk=chair.id)[0:6]

    return render(request, "store/chair_detail.html", {"chair" : chair ,"chairs" : chairs , "comments" : comments})

def delete_chair_view(request: HttpRequest , chair_id: int):

    chair = Chair.objects.get(pk=chair_id)

    chair.delete()
    return redirect('main:home_view')

def update_chair_view(request: HttpRequest, chair_id: int):
    chair = Chair.objects.get( pk=chair_id)

    if request.method == "POST":
        chair.name = request.POST["name"]
        chair.color = request.POST["color"]
        chair.material = request.POST["material"]
        chair.adjustable = request.POST["adjustable"]
        chair.max_weight = request.POST["max_weight"]
        chair.price = request.POST["price"]

        if "image" in request.FILES:
            chair.image = request.FILES["image"]

        chair.save()
        return redirect('store:chair_detail_view', chair_id=chair.id)

    return render(request, "store/update_chair.html", {"chair": chair})

def add_headset_view(request: HttpRequest):
    
    if request.method == "POST":
        new_headset = Headset(
            name=request.POST["name"],
            connection_type=request.POST["connection_type"],
            has_microphone=request.POST["has_microphone"],
            price=request.POST["price"],
            image=request.FILES["image"],
        )
        new_headset.save()
        return redirect('main:home_view')
    
    return render(request, "store/add_headset.html")

def headset_detail_view(request: HttpRequest , headset_id :int):
    headset = Headset.objects.get(pk=headset_id)
    comments = Headset_comment.objects.filter(headset=headset)
    headsets = Headset.objects.filter(category=headset.category).exclude(pk=headset.id)[0:6]

    return render(request, "store/headset_detail.html", {"headset" : headset ,"headsets" : headsets , "comments" : comments })

def delete_headset_view(request: HttpRequest , headset_id :int):

    headset = Headset.objects.get(pk=headset_id)

    headset.delete()
    return redirect('main:home_view')




def update_headset_view(request: HttpRequest, headset_id: int):
    headset = Headset.objects.get( pk=headset_id)

    if request.method == "POST":
        headset.name = request.POST["name"]
        headset.connection_type = request.POST["connection_type"]
        headset.has_microphone = request.POST["has_microphone"]
        headset.price = request.POST["price"]

        if "image" in request.FILES:
            headset.image = request.FILES["image"]

        headset.save()
        return redirect('store:headset_detail_view', headset_id=headset.id)

    return render(request, "store/update_headset.html", {"headset": headset})

def add_keyboard_view(request: HttpRequest):
    if request.method == "POST":
        new_keyboard = Keyboard(
            name=request.POST["name"],
            type=request.POST["type"],
            language=request.POST["language"],
            price=request.POST["price"],
            image=request.FILES["image"],
        )
        new_keyboard.save()
        return redirect('main:home_view')
    
    return render(request, "store/add_keyboard.html")

def update_keyboard_view(request: HttpRequest, keyboard_id: int):
    keyboard = Keyboard.objects.get(pk=keyboard_id)
  

    if request.method == "POST":
        keyboard.name = request.POST["name"]
        keyboard.type = request.POST["type"]
        keyboard.language = request.POST["language"]
        keyboard.price = request.POST["price"]

        if "image" in request.FILES:
            keyboard.image = request.FILES["image"]

        keyboard.save()
        return redirect('store:keyboard_detail_view' , keyboard_id=keyboard.id)

    return render(request, "store/update_keyboard.html", {"keyboard": keyboard})

def delete_keyboard_view(request: HttpRequest , keyboard_id :int):

    keyboard = Keyboard.objects.get(pk=keyboard_id)

    keyboard.delete()
    return redirect('main:home_view')


def keyboard_detail_view(request: HttpRequest , keyboard_id :int):
    keyboard = Keyboard.objects.get(pk=keyboard_id)
    comments = Keyboard_comment.objects.filter(keyboard=keyboard)
    keyboards = Keyboard.objects.filter(category=keyboard.category).exclude(pk=keyboard.id)[0:6]

    return render(request, "store/keyboard_detail.html", {"keyboard" : keyboard ,"keyboards" : keyboards , "comments" : comments })


def search_view(request):
    if "category" in request.GET:
        category = request.GET["category"]
    else:
        category = "all"

    if "search" in request.GET:
        search_query = request.GET["search"]
    else:
        search_query = ""

    pcs = monitors = mouses = chairs = headsets = keyboards = []

    if category == "all":
        if search_query:
            pcs = PC.objects.filter(name__icontains=search_query)
            monitors = Monitor.objects.filter(name__icontains=search_query)
            mouses = Mouse.objects.filter(name__icontains=search_query)
            chairs = Chair.objects.filter(name__icontains=search_query)
            headsets = Headset.objects.filter(name__icontains=search_query)
            keyboards = Keyboard.objects.filter(name__icontains=search_query)
        else:
            pcs = PC.objects.all()
            monitors = Monitor.objects.all()
            mouses = Mouse.objects.all()
            chairs = Chair.objects.all()
            headsets = Headset.objects.all()
            keyboards = Keyboard.objects.all()

    elif category == "pc":
        pcs = PC.objects.filter(name__icontains=search_query) if search_query else PC.objects.all()

    elif category == "monitor":
        monitors = Monitor.objects.filter(name__icontains=search_query) if search_query else Monitor.objects.all()

    elif category == "mouse":
        mouses = Mouse.objects.filter(name__icontains=search_query) if search_query else Mouse.objects.all()

    elif category == "chair":
        chairs = Chair.objects.filter(name__icontains=search_query) if search_query else Chair.objects.all()

    elif category == "headset":
        headsets = Headset.objects.filter(name__icontains=search_query) if search_query else Headset.objects.all()

    elif category == "keyboard":
        keyboards = Keyboard.objects.filter(name__icontains=search_query) if search_query else Keyboard.objects.all()

    return render(request, "store/search.html", {
        "pcs": pcs,
        "monitors": monitors,
        "mouses": mouses,
        "chairs": chairs,
        "headsets": headsets,
        "keyboards": keyboards,
    })


def pc_comment_view(request: HttpRequest , pc_id: int ):
    pc = PC.objects.get(pk=pc_id)

    if request.method == "POST":

        new_comment = PC_comment(
                pc = pc, #pc from db = pc object 
                full_name=request.POST["full_name"],
                content=request.POST["content"],
        )    
        new_comment.save()
        return redirect("store:pc_detail_view" , pc_id = pc_id)
    
def monitor_comment_view(request: HttpRequest , monitor_id: int ):
    monitor = Monitor.objects.get(pk=monitor_id)

    if request.method == "POST":

        new_comment = Monitor_comment(
                monitor =  monitor, #monitor from db = monitor object 
                full_name=request.POST["full_name"],
                content=request.POST["content"],
        )    
        new_comment.save()
        return redirect("store:monitor_detail_view" , monitor_id = monitor_id)
    

def headset_comment_view(request: HttpRequest , headset_id: int ):
    headset = Headset.objects.get(pk=headset_id)

    if request.method == "POST":

        new_comment = Headset_comment(
                headset =  headset, #headset from db = headset object 
                full_name=request.POST["full_name"],
                content=request.POST["content"],
        )    
        new_comment.save()
        return redirect("store:headset_detail_view" , headset_id = headset_id)
    

def mouse_comment_view(request: HttpRequest , mouse_id: int ):
    mouse = Mouse.objects.get(pk=mouse_id)

    if request.method == "POST":

        new_comment = Mouse_comment(
                mouse =  mouse, #mouse from db = mouse object 
                full_name=request.POST["full_name"],
                content=request.POST["content"],
        )    
        new_comment.save()
        return redirect("store:mouse_detail_view" , mouse_id = mouse_id)
    

def keyboard_comment_view(request: HttpRequest , keyboard_id: int ):
    keyboard = Keyboard.objects.get(pk=keyboard_id)

    if request.method == "POST":

        new_comment = Keyboard_comment(
                keyboard =  keyboard, #keyboard from db = keyboard object 
                full_name=request.POST["full_name"],
                content=request.POST["content"],
        )    
        new_comment.save()
        return redirect("store:keyboard_detail_view" , keyboard_id = keyboard_id)


def chair_comment_view(request: HttpRequest , chair_id: int ):
    chair = Chair.objects.get(pk=chair_id)

    if request.method == "POST":

        new_comment = Chair_comment(
                chair =  chair, #chair from db = chair object 
                full_name=request.POST["full_name"],
                content=request.POST["content"],
        )    
        new_comment.save()
        return redirect("store:chair_detail_view" , chair_id = chair_id)
   
def admin_pc_view(request):
    pcs = PC.objects.all()
    return render(request, 'store/pcs_admin.html', {'pcs': pcs})

def admin_monitor_view(request):
    monitors = Monitor.objects.all()
    return render(request, 'store/monitors_admin.html', {'monitors': monitors})

def admin_mouse_view(request):
    mouses = Mouse.objects.all()
    return render(request, 'store/mouses_admin.html', {'mouses': mouses})

def admin_headset_view(request):
    headsets = Headset.objects.all()
    return render(request, 'store/headsets_admin.html', {'headsets': headsets})

def admin_keyboard_view(request):
    keyboards = Keyboard.objects.all()
    return render(request, 'store/keyboards_admin.html', {'keyboards': keyboards})

def admin_chair_view(request):
    chairs = Chair.objects.all()
    return render(request, 'store/chairs_admin.html', {'chairs': chairs})


MODEL_MAP = {
    "PC": PC,
    "Monitor": Monitor,
    "Keyboard": Keyboard,
    "Mouse": Mouse,
    "Headset": Headset,
    "Chair": Chair,
}
def add_to_cart(request, category, product_id):
    cart = request.session.get('cart', {})

    if category not in cart:
        cart[category] = {}

    cart[category][str(product_id)] = cart[category].get(str(product_id), 0) + 1

    request.session['cart'] = cart
    return redirect('store:cart_view')
 
def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total_price = 0

    for category, products in cart.items():
        model = MODEL_MAP.get(category)
        if not model:
            continue
        for product_id, quantity in products.items():
            product = model.objects.get(pk=product_id)
            subtotal = product.price * quantity
            items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal,
                'category': category,
            })
            total_price += subtotal

    return render(request, 'store/cart.html', {
        'items': items,
        'total_price': total_price
    })
    
def remove_from_cart(request, category, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if category in cart and product_id in cart[category]:
        del cart[category][product_id]
        if not cart[category]:  
            del cart[category]

    request.session['cart'] = cart
    return redirect('store:cart_view')

def checkout_view(request):
    return render(request, 'store/checkout.html')

def process_payment(request):
    if request.method == 'POST':
        return redirect('store:payment_success') 
    return redirect('store:cart_view')

def payment_success(request):
    return render(request, 'store/payment_success.html')
